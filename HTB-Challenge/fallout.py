import subprocess

# Constants for weights of each skill
health_weight = 0.2
agility_weight = 0.3
charisma_weight = 0.1
knowledge_weight = 0.05
energy_weight = 0.05
resourcefulness_weight = 0.3

# Function to calculate skill score
def calculate_skill_score(skill_score, weight):
    return round(6 * (int(skill_score) * weight)) + 10

# Function to calculate overall value
def calculate_overall_value(health, agility, charisma, knowledge, energy, resourcefulness):
    return round(5 * ((health * 0.18) + (agility * 0.20) + (charisma * 0.21) + (knowledge * 0.08) + (energy * 0.17) + (resourcefulness * 0.16)))

# Connect to the server and retrieve candidates' data
cmd = "nc 94.237.53.113 50111"
process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

if process.returncode != 0:
    print(f"Failed to connect to the server: {stderr.decode()}")
    exit(1)

# Extract candidates' data from server response
candidates_data = stdout.decode().strip().split('\n')

# Initialize a list to store candidate information
candidates_info = []

# Process each candidate's data
for candidate in candidates_data:
    candidate_data = candidate.strip().split(',')
    name = candidate_data[0].strip()
    surname = candidate_data[1].strip()
    health_score = calculate_skill_score(candidate_data[2], health_weight)
    agility_score = calculate_skill_score(candidate_data[3], agility_weight)
    charisma_score = calculate_skill_score(candidate_data[4], charisma_weight)
    knowledge_score = calculate_skill_score(candidate_data[5], knowledge_weight)
    energy_score = calculate_skill_score(candidate_data[6], energy_weight)
    resourcefulness_score = calculate_skill_score(candidate_data[7], resourcefulness_weight)
    
    overall_value = calculate_overall_value(health_score, agility_score, charisma_score,
                                            knowledge_score, energy_score, resourcefulness_score)
    
    candidates_info.append((name + ' ' + surname, overall_value))

# Sort candidates by overall value in descending order
candidates_info.sort(key=lambda x: x[1], reverse=True)

# Select top 14 candidates
top_candidates = candidates_info[:14]

# Format the output as required
output = ', '.join(f"{name} - {score}" for name, score in top_candidates)

print(output)

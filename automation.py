import pandas as pd 

def search_keywords(excel_file_path, keywords):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(excel_file_path,'2016')

    # Initialize an empty list to store IAD numbers 
    matched_iads = []

    # Iterate through each row in the Dataframe
    for index, row in df.iterrows():
        # Extract the description from the 'description' column (5th column)
        description = str(row[5])
        # Check if any keyword from the keywords list is present in the description
        if any(keyword.lower() in description.lower() for keyword in keywords):
            # If matched, add the IAD number to the list (IAD #'s on the 3rd column)
            #Also finding new uncoded excessive force and racial bias incidents
            if("Use of Force" not in str(row[4]) and "BIAS-Free Policing Policy" not in str(row[4])):
                matched_iads.append(row[3])
    seen_iads = set()

# Initialize an empty list to store unique IDs in order
    unique_matched_iads  = []

# Loop through the list
    for id in matched_iads:
    # Check if the ID has not been seen before
        if id not in seen_iads:
        # Add the ID to the set of seen IDs
            seen_iads.add(id)
        
        # Add the unique ID to the list
            unique_matched_iads.append(id)    

    # Return the list of matched iAd numbers
    return unique_matched_iads

# Example usage:
excel_file_path = '2016_2019_data.xlsx' #2016 BPD file that was provided to us
keywords = {
    "Abusing",
    "Assault",
    "Force",
    "F word",
    "Race",
    "Pushed",
    "Beating",
    "Homophobic",
    "Racist",
    "African Americans",
    "Discriminatory",
    "Slavery",
    "Excessive",
    "Dragged",
    "Threw",
    "Profanity",
    "Choke",
    "Illegal",
    "Profiled",
    "Profiling",
    "Harassment",
    "Violent",
    "Thrown",
    "Drunk",
    "Tazer",
    "Cried",
    "Hurting",
    "Pushed",
    "Cursed",
    "Threatened",
    "B word",
    "Stupid",
    "Lunatic",
    "Scared",
    "Shaking",
    "Yelled",
    "Alcoholic",
    "Unauthorized",
    "Harassed",
    "No cause",
    "Trauma",
    "Injury",
    "Injured",
    "injure",
    "Banged",
    "banging",
    "bang",
    "Bruised",
    "Bruise",
    "Damaged",
    "Damage",
    "damaging",
    "Unjustly",
    "Unjust",
    "No justification",
    "Unjustified",
    "Middle finger",
    "Targeted",
    "Victimized",
    "Roughly",
    "Grabbed",
    "Bruises",
    "Disability",
    "Frightened",
    "Stubborn",
    "Demanding",
    "Demanded",
    "No explanation",
    "Loud",
    "Insulting",
    "Abuse",
    "Disrespect",
    "Belligerent",
    "Bothered",
    "Untruthful",
    "Erratic",
    "Yelling",
    "Yelled",
    "Yell",
    "Rude",
    "Attack",
    "Refuse",
    "Refused",
    "Harming",
    "Harm",
    "Harmful",
    "Harmed",
    "Upset",
    "Unprofessional",
    "Brown",
    "Muslim",
    "Dislocated",
    "Racists",
    "Racist",
    "Guns",
    "Gun",
    "Weapons",
    "Weapon",
    "Drugs",
    "Substance possession",
    "Substance",
    "Under the influence",
    "Violation",
    "Profanity",
    "Profane",
    "Choking",
    "Screamed",
    "Scream",
    "Brutalized",
    "Brutal",
    "Hispanic",
    "A word",
    "Intimidated",
    "Coerced",
    "Negligence",
    "Reckless",
    "Misconduct",
    "Unlawful",
    "Malicious",
    "Provoked",
    "Provocation",
    "Offensive",
    "Degrading",
    "Invasive",
    "Menacing",
    "Inhumane",
    "Intolerance",
    "Unjustifiable",
    "Prejudiced",
    "Prejudice",
    "Unequal",
    "Abhorrent",
    "Brutality",
    "Injustice",
    "Discrimination",
    "Racial profiling",
    "Disproportionate",
    "Unequal treatment",
    "Abnormal",
    "Aggressive",
    "Hostile",
    "Agitation",
    "Confrontation",
    "Condemn",
    "Exploitation",
    "Invasive",
    "Intrusive",
    "Provocative",
    "Antagonistic",
    "Offensive",
    "Insensitivity",
    "Prejudiced",
    "Racial slurs",
    "Unethical",
    "Bias",
    "Bigotry",
    "Derogatory",
    "Demeaning",
    "Detained",
    "Repression",
    "Oppression",
    "Terrorize",
    "Violate",
    "Violation",
    "Agony",
    "Menace",
    "Harsh",
    "Dreadful",
    "Dehumanize",
    "Subjugate",
    "Fear",
    "Panic",
    "Mistreatment",
    "Infringement",
    "Aberrant",
    "Outrageous",
    "Despicable",
    "Invasive",
    "Vile",
    "Abhorrent",
    "Deplorable",
    "Inferior",
    "Degradation",
    "Bullying",
    "Coercion",
    "Condemnation",
    "Provocative",
    "Harsh",
    "Maltreatment",
    "Reproach",
    "Provoking",
    "Cruelty",
    "Torture"
}  # Replace with keywords that we find

result = search_keywords(excel_file_path, keywords) #calling the function
print("Matched IAD numbers:", result)
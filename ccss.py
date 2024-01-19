import math

def round_to_1_decimal(value):
    return round(value, 1)

def calculate_cvss_base_score(ConfImpact, IntegImpact, AvailImpact, AccessVector, Authentication, AccessComplexity):
    Impact = 10.41 * (1 - (1 - ConfImpact) * (1 - IntegImpact) * (1 - AvailImpact))
    Exploitability = 20 * AccessVector * Authentication * AccessComplexity
    f_Impact = 1.176 if Impact != 0 else 0
    BaseScore = round_to_1_decimal(((0.6 * Impact) + (0.4 * Exploitability) - 1.5) * f_Impact)
    return BaseScore

def get_input(prompt, mapping, default_value):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            return default_value
        if user_input.isdigit() and int(user_input) in mapping:
            return mapping[int(user_input)]
        for key, value in mapping.items():
            if user_input == str(value):
                return value
        print("Invalid input. Please try again or press Enter for the default most severe answer.")

def cli():
    print("CCSS Base Score Calculator\n")
    print("""Instructions:
For each category, enter the number corresponding to your selection.
If you want to use the default most severe answer, simply press Enter.
For example, for Impact: 1 - None, 2 - Partial, 3 - Complete, default - Complete.
""")

    flaw_name = input("Enter the name of the configuration flaw: ")

    mappings = {
        'AccessVector': {1: 0.395, 2: 0.646, 3: 1.0},
        'Authentication': {1: 0.45, 2: 0.56, 3: 0.704},
        'AccessComplexity': {1: 0.35, 2: 0.61, 3: 0.71},
        'Impact': {1: 0.0, 2: 0.275, 3: 0.660},
    }

    defaults = {
        'AccessVector': mappings['AccessVector'][3],
        'Authentication': mappings['Authentication'][3],
        'AccessComplexity': mappings['AccessComplexity'][3],
        'Impact': mappings['Impact'][3],
    }

    prompts = {
        'AccessVector': "Access Vector (1 - Local, 2 - Adjacent, 3 - Network): ",
        'Authentication': "Authentication (1 - Multiple, 2 - Single, 3 - None): ",
        'AccessComplexity': "Access Complexity (1 - High, 2 - Medium, 3 - Low): ",
        'ConfidentialityImpact': "Confidentiality Impact (1 - None, 2 - Partial, 3 - Complete): ",
        'IntegrityImpact': "Integrity Impact (1 - None, 2 - Partial, 3 - Complete): ",
        'AvailabilityImpact': "Availability Impact (1 - None, 2 - Partial, 3 - Complete): ",
    }

    ConfImpact = get_input(prompts['ConfidentialityImpact'], mappings['Impact'], defaults['Impact'])
    IntegImpact = get_input(prompts['IntegrityImpact'], mappings['Impact'], defaults['Impact'])
    AvailImpact = get_input(prompts['AvailabilityImpact'], mappings['Impact'], defaults['Impact'])
    AccessVector = get_input(prompts['AccessVector'], mappings['AccessVector'], defaults['AccessVector'])
    Authentication = get_input(prompts['Authentication'], mappings['Authentication'], defaults['Authentication'])
    AccessComplexity = get_input(prompts['AccessComplexity'], mappings['AccessComplexity'], defaults['AccessComplexity'])

    base_score = calculate_cvss_base_score(
        ConfImpact,
        IntegImpact,
        AvailImpact,
        AccessVector,
        Authentication,
        AccessComplexity
    )

    print(f"\nThe base score for '{flaw_name}' is: {base_score}")

if __name__ == "__main__":
    cli()

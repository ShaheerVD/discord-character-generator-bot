import random
import characterParameters


#create character
class Character:
    def __init__(self, gender, age, body_type, hair, clothes, weapon, occupation, theme):
        self.gender = gender
        self.age = age
        self.body_type = body_type
        self.hair = hair
        self.clothes = clothes
        self.weapon = weapon
        self.occupation = occupation
        self.theme = theme

#Get random array value
def get_random_option(option):
  index = random.randrange(len(option))
  return option[index]

#GenerateCharacterMethod
def generate_character():
    # Select random options for each parameter
    gender = get_random_option(characterParameters.GENDERS)
    age = get_random_option(characterParameters.AGE)
    body = get_random_option(characterParameters.BODY)
    hair = get_random_option(characterParameters.HAIR)
    clothes = get_random_option(characterParameters.CLOTHES)
    occupation = get_random_option(characterParameters.OCCUPATION)
    weapon = get_random_option(characterParameters.WEAPON)
    theme = get_random_option(characterParameters.THEME)

    return Character(gender, age, body, hair, clothes, weapon, occupation, theme)


  


def get_response(user_input:str) -> str:
  lowered: str = user_input.lower()

  if lowered =='!generate':
     # Generate Character
        Character = generate_character()

        # Format character details into a message
        message = "Generated Character:\n"
        message += f"Gender: {Character.gender}\n"
        message += f"Age: {Character.age}\n"
        message += f"Body Type: {Character.body_type}\n"
        message += f"Hairstyle: {Character.hair}\n"
        message += f"Clothing Style: {Character.clothes}\n"
        message += f"Occupation: {Character.occupation}\n"
        message += f"Weapon Type: {Character.weapon}\n"
        message += f"Theme: {Character.theme}"

        return message
        
  

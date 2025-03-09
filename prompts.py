import streamlit as st


def userInput():
    st.subheader("Character Details")
    name = st.text_input("Character Name:")
    race = st.text_input("Race:")
    char_class = st.text_input("Class:")
    subclass = st.text_input("Subclass:")
    background = st.text_input("Background:")
    personality = st.text_input("Personality:")
    physical_characteristics = st.text_area("Physical Characteristics:")
    
    return f"""
            these are some examples

            Example1
            Thaldrin Ironfist – The Exiled Warrior Seeking Redemption  
            **Character Name:** Thaldrin Ironfist  
            **Race:** Dwarf  
            **Class:** Fighter  
            **Subclass:** Battle Master  
            **Background:** Soldier  
            **Personality Traits:** Stubborn, loyal, tactically minded  
            **Physical Characteristics:** Male, stocky build, deeply tanned skin, long braided auburn beard, battle-worn face with scars across his left cheek  

            **Backstory:**  
            Thaldrin Ironfist was born in the ancient dwarven citadel of Hammerhold, where every child's cradle was rocked by the distant clang of the forge. Raised on tales of honor and battle, he idolized his father, a legendary warrior of the Iron Guard. But when a goblin horde breached their mountain home, Thaldrin's father fell in battle, leaving behind a legacy too great to ignore.  

            Determined to make his father proud, Thaldrin enlisted in the Iron Guard, proving himself a master of battlefield tactics. Yet war reveals not just heroes but traitors. During a brutal siege against orcish invaders, Thaldrin's commanding officer betrayed their unit, selling intelligence that led to the massacre of his battalion. Framed for cowardice and desertion, he was dishonorably discharged and exiled from his homeland.  

            Now, he wanders as a mercenary, his every action driven by an unrelenting desire to clear his name. The weight of his father's legacy presses down on him, and every battle is another chance to prove himself worthy of the title stolen from him. Though his heart burns for revenge, he knows that honor is not found in vengeance—but in justice.  

            **Story Hooks:**  
            - A chance encounter with a survivor from his battalion who holds proof of his innocence.  
            - A lost dwarven artifact that could restore his honor if recovered.  
            - An aging warrior who fought alongside his father, revealing secrets about his past.  

            **Adobe Firefly Art Prompt:**  
            "A stocky dwarf warrior with a battle-worn face, long braided auburn beard, and deep scars across his left cheek. His plate armor is engraved with intricate dwarven runes, and his heavy war axe gleams in torchlight. The backdrop is a crumbling mountain fortress, mist swirling around him as he grips his weapon with steely resolve. His gaze is hardened, filled with years of loss and battle. Cinematic lighting, high detail, fantasy realism."

            ---

            Example 2

            Sylvaris Moonshadow – The Shadow of a Forgotten House  
            **Character Name:** Sylvaris Moonshadow  
            **Race:** Elf  
            **Class:** Rogue  
            **Subclass:** Arcane Trickster  
            **Background:** Criminal  
            **Personality Traits:** Charming, cunning, unpredictable  
            **Physical Characteristics:** Male, tall and lean, silver hair flowing past his shoulders, piercing emerald eyes, sharp angular features  

            **Backstory:**  
            Born into the noble House Moonshadow, Sylvaris was expected to follow the path of diplomacy, arcane study, and honor. But while his siblings memorized political treatises, he explored the hidden tunnels beneath the palace, perfecting the art of slipping through shadows unseen.  

            At sixteen, his world shattered. An ancient elven artifact—an heirloom of great power—was stolen, and the blame fell upon him. Betrayed by his own family, branded a traitor, and sentenced to death, he barely escaped with his life. Fleeing into the underbelly of the city, he became a ghost in the streets, mastering deception, magic, and the art of survival.  

            Now, Sylvaris thrives as a legendary thief, stealing from those who betrayed him and outwitting the very nobles who once cast him aside. But deep down, he is still haunted by a single question—who truly stole the artifact, and why frame him? The answer could restore his name… or destroy him forever.  

            **Story Hooks:**  
            - A masked informant offers information about the true thief—for a dangerous price.  
            - A high-stakes heist that requires breaking into his own family's ancestral vault.  
            - A noble heir who wears the very artifact he was accused of stealing.  

            **Adobe Firefly Art Prompt:**  
            "A tall, lean elf rogue with flowing silver hair and piercing emerald eyes, dressed in dark leather armor adorned with glowing arcane runes. He smirks as he twirls a dagger crackling with magical energy. The scene is a dimly lit alleyway, mist rolling through the cobbled streets, faint city lights glimmering in the background. The atmosphere is mysterious and foreboding, with a sense of intrigue and danger. Fantasy realism, high detail, moody lighting."

            Now, generate a new character using the following input:
            **Name:** {name}
            **Race:** {race}
            **Class:** {char_class}
            **Subclass:** {subclass}
            **Background:** {background}
            **Personality:** {personality}
            **Physical Characteristics:** {physical_characteristics}
            **Provide:**  
            - A deep and compelling backstory  
            - Three engaging story hooks  
            - An Adobe Firefly image generation prompt  
            ---
            """








    
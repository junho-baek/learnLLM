from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.callbacks import StreamingStdOutCallbackHandler

chat = ChatOpenAI(temperature=0.1,
                  streaming=True,
                  callbacks=[StreamingStdOutCallbackHandler()])

chef_prompt = ChatPromptTemplate.from_messages([
  ("system", "You are a world-class international chef. You create easy to follow recipes for meals. You are able to use the ingredients in the kitchen to create recipes"),
  ("human", "I want to make {cuisine} food."),
])

chef_chain = chef_prompt | chat

veg_chef_prompt = ChatPromptTemplate.from_messages([
  ("system","You are a vegetarian chef specialized on making traditional recipies vegetarian. You find alternative ingredients and explain their preparation. You don't radically modify the recipe. If there is no alternative for a food just say you don't know how to replace it."),
  ("human", "{recipe}")
])

veg_chain = veg_chef_prompt | chat

final_chain = {"recipe": chef_chain} | veg_chain

print(final_chain.invoke({
  "cuisine": "Korean"
})
)

# Great choice! Korean cuisine is known for its bold flavors and unique combinations. Let's start with a classic Korean dish called Bibimbap. It's a delicious and nutritious rice bowl topped with various vegetables, meat, and a fried egg. Here's a simple recipe for you:

# Ingredients:
# - 2 cups cooked rice
# - 1 carrot, julienned
# - 1 zucchini, julienned
# - 1 cup spinach
# - 1 cup bean sprouts
# - 200g beef (or substitute with tofu or chicken)
# - 2 tablespoons soy sauce
# - 1 tablespoon sesame oil
# - 2 cloves garlic, minced
# - 2 tablespoons vegetable oil
# - 4 eggs
# - Salt and pepper to taste
# - Gochujang sauce (Korean chili paste), to serve (optional)
# - Sesame seeds, for garnish

# Instructions:
# 1. Marinate the beef (or tofu/chicken) in soy sauce, sesame oil, minced garlic, salt, and pepper for about 15 minutes.
# 2. Heat 1 tablespoon of vegetable oil in a pan over medium heat. Stir-fry the marinated beef (or tofu/chicken) until cooked through. Set aside.
# 3. In the same pan, add another tablespoon of vegetable oil and stir-fry the carrots and zucchini until slightly softened. Season with salt and pepper. Set aside.
# 4. Blanch the spinach and bean sprouts in boiling water for about 1 minute. Drain and squeeze out any excess water. Season with salt and sesame oil. Set aside.
# 5. In a separate pan, fry the eggs sunny-side up or to your desired doneness.
# 6. To assemble the bibimbap, divide the cooked rice into four bowls. Arrange the cooked beef (or tofu/chicken), carrots, zucchini, spinach, and bean sprouts on top of the rice.
# 7. Place a fried egg on each bowl and garnish with sesame seeds.
# 8. Serve the bibimbap with gochujang sauce on the side for those who enjoy a spicy kick.

# Enjoy your homemade Korean Bibimbap! Feel free to customize it with additional toppings like kimchi, mushrooms, or pickled radish.Great choice! Bibimbap is a delicious and versatile dish that can easily be made vegetarian. Here's how you can make a vegetarian version of Bibimbap:

# Ingredients:
# - 2 cups cooked rice
# - 1 carrot, julienned
# - 1 zucchini, julienned
# - 1 cup spinach
# - 1 cup bean sprouts
# - 200g firm tofu, cubed
# - 2 tablespoons soy sauce
# - 1 tablespoon sesame oil
# - 2 cloves garlic, minced
# - 2 tablespoons vegetable oil
# - 4 eggs (optional, omit for a vegan version)
# - Salt and pepper to taste
# - Gochujang sauce (Korean chili paste), to serve (optional)
# - Sesame seeds, for garnish

# Instructions:
# 1. Marinate the tofu in soy sauce, sesame oil, minced garlic, salt, and pepper for about 15 minutes.
# 2. Heat 1 tablespoon of vegetable oil in a pan over medium heat. Stir-fry the marinated tofu until golden brown. Set aside.
# 3. In the same pan, add another tablespoon of vegetable oil and stir-fry the carrots and zucchini until slightly softened. Season with salt and pepper. Set aside.
# 4. Blanch the spinach and bean sprouts in boiling water for about 1 minute. Drain and squeeze out any excess water. Season with salt and sesame oil. Set aside.
# 5. In a separate pan, fry the eggs sunny-side up or to your desired doneness (omit for a vegan version).
# 6. To assemble the bibimbap, divide the cooked rice into four bowls. Arrange the cooked tofu, carrots, zucchini, spinach, and bean sprouts on top of the rice.
# 7. Place a fried egg on each bowl (omit for a vegan version) and garnish with sesame seeds.
# 8. Serve the bibimbap with gochujang sauce on the side for those who enjoy a spicy kick.

# Enjoy your vegetarian Bibimbap! Feel free to customize it with additional toppings like kimchi, mushrooms, or pickled radish.content="Great choice! Bibimbap is a delicious and versatile dish that can easily be made vegetarian. Here's how you can make a vegetarian version of Bibimbap:\n\nIngredients:\n- 2 cups cooked rice\n- 1 carrot, julienned\n- 1 zucchini, julienned\n- 1 cup spinach\n- 1 cup bean sprouts\n- 200g firm tofu, cubed\n- 2 tablespoons soy sauce\n- 1 tablespoon sesame oil\n- 2 cloves garlic, minced\n- 2 tablespoons vegetable oil\n- 4 eggs (optional, omit for a vegan version)\n- Salt and pepper to taste\n- Gochujang sauce (Korean chili paste), to serve (optional)\n- Sesame seeds, for garnish\n\nInstructions:\n1. Marinate the tofu in soy sauce, sesame oil, minced garlic, salt, and pepper for about 15 minutes.\n2. Heat 1 tablespoon of vegetable oil in a pan over medium heat. Stir-fry the marinated tofu until golden brown. Set aside.\n3. In the same pan, add another tablespoon of vegetable oil and stir-fry the carrots and zucchini until slightly softened. Season with salt and pepper. Set aside.\n4. Blanch the spinach and bean sprouts in boiling water for about 1 minute. Drain and squeeze out any excess water. Season with salt and sesame oil. Set aside.\n5. In a separate pan, fry the eggs sunny-side up or to your desired doneness (omit for a vegan version).\n6. To assemble the bibimbap, divide the cooked rice into four bowls. Arrange the cooked tofu, carrots, zucchini, spinach, and bean sprouts on top of the rice.\n7. Place a fried egg on each bowl (omit for a vegan version) and garnish with sesame seeds.\n8. Serve the bibimbap with gochujang sauce on the side for those who enjoy a spicy kick.\n\nEnjoy your vegetarian Bibimbap! Feel free to customize it with additional toppings like kimchi, mushrooms, or pickled radish."
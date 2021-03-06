from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, User, Category, Recipe


engine = create_engine('sqlite:///recipes.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create initial user to associate recipes
user1 = User(name="Admin Bob",
             email="admin_bob@gmail.com",
             picture="https://www.publicdomainpictures.net/pictures/270000/velka/apple-piepieicon-sign-food-d.jpg")
session.add(user1)
session.commit()


category1 = Category(user_id=1, name="breakfast")
session.add(category1)
session.commit()
breakfast1 = Recipe(user_id=1,
                    name="French Toast",
                    instructions="""Place bread cubes in an instant pot. For
                    chewier French toast, leave the bread out overnight to get
                    slightly stale. Combine all other ingredients in a mixing
                    bowl and whisk to combine. Pour the mixture over the bread
                    cubes in the instant pot and gently toss to ensure
                    everything is evenly coated. Secure the lid and set to cook
                    for 20 minutes. When cooking is complete, release pressure
                    and remove the lid, then transfer the French toast cubes
                    to a serving dish or plates and serve with additional
                    syrup, butter, powdered sugar or whipped cream.""",
                    ingredients='8 Thick-cut slices of French bread, cubed\r'
                                '2 Eggs\r'
                                '1 Cup milk\r'
                                '2 Teaspoons vanilla extract\r'
                                '2 Tablespoons ground cinnamon\r'
                                '1/2 Teaspoon ground ginger',
                    category=category1)
session.add(breakfast1)
session.commit()
breakfast2 = Recipe(user_id=1,
                    name="Chai Pancakes",
                    instructions="""In a large bowl, whisk together the egg,
                    milk, butter, sugar and vanilla. In a separate bowl, stir
                    together cinnamon, cloves, nutmeg, ginger, salt, flour and
                    baking powder. Add the wet to the dry and, using a spatula,
                    mix just until combined. Heat a pan or skillet over medium
                    heat and drop in 1/3 cup of the batter at a time. Flip once
                    when first side is golden brown. Continue until all batter
                    is cooked. Top with maple syrup and serve warm.""",
                    ingredients='1 Egg\r'
                                '1 1/4 Cup milk\r'
                                '3 Tablespoons melted butter\r'
                                '1 Tablespoon sugar\r'
                                '1 Teaspoon vanilla\r'
                                '1 Teaspoon cinnamon\r'
                                '1/2 Teaspoon ground cloves\r'
                                '1/2 Teaspoon ground nutmeg\r'
                                '1/2 Teaspoon ground ginger\r'
                                '1 Teaspoon salt\r'
                                '1 1/2 Cups flour\r'
                                '3 1/2 Teaspoons baking powder',
                    category=category1)
session.add(breakfast2)
session.commit()
breakfast3 = Recipe(user_id=1,
                    name="Breakfast Egg Muffins",
                    instructions="""Whisk together the eggs in a large bowl. Add
                    the salt, pepper, garlic powder, onion, green pepper, bacon,
                    and Cheddar and combine all ingredients. Line a muffin tin
                    with paper liners (these egg muffins love to stick even with
                    spray, so liners work best). Spoon the mixture into each
                    cup of the muffin tin; fill approximately 3/4 full as these
                    will puff up as they cook. Bake in a 350 degree oven for
                    about 20 minutes or until set. Serve hot.""",
                    ingredients='12 eggs\r'
                                '1/4 teaspoon pepper\r'
                                '1/2 teaspoon salt\r'
                                '1/2 teaspoon garlic powder\r'
                                '1/2 an onion, chopped'
                                '1/2 of a green pepper, chopped\r'
                                '1/2 cup cooked bacon, chopped',
                    category=category1)
session.add(breakfast3)
session.commit()


category2 = Category(user_id=1, name="appetizers")
session.add(category2)
session.commit()
appetizer1 = Recipe(user_id=1,
                    name="Avocado Fries with Lime Dipping Sauce",
                    instructions="""Preheat the oven 425F, follow directions
                    above and bake on a sheet pan until golden and crisp, 10 to
                    15 minutes. Place egg in a shallow bowl. On another plate,
                    combine panko with 1 teaspoon Tajin. Season avocado wedges
                    with 1/4 teaspoon Tajin.  Dip each piece first in egg, and
                    then in panko. Spray both sides with oil then transfer to
                    the air fryer and cook 7 to 8 minutes turning halfway.
                    Serve hot with dipping sauce.""",
                    ingredients='8 ounces (2 small) avocados, peeled, pitted and cut into 16 wedges\r'
                                '1 large egg, lightly beaten\r'
                                '3/4 cup panko breadcrumbs (I used gluten-free)\r'
                                '1 1/4 teaspoons lime chili seasoning salt, such as Tajin Classic\r'
                                'For the lime dipping sauce:\r'
                                '1/4 cup 0% Greek Yogurt\r'
                                '3 tablespoons light mayonnaise\r'
                                '2 teaspoons fresh lime juice\r'
                                '1/2 teaspoon lime chili seasoning salt, such as Tajin Classic\r'
                                '1/8 teaspoon kosher salt',
                    category=category2)
session.add(appetizer1)
session.commit()
appetizer2 = Recipe(user_id=1,
                    name="Basil Aioli with Crudites",
                    instructions="""Combine first 6 ingredients in a food
                    processor, and process until smooth. (Will keep, covered in
                    refrigerator, up to 2 days.) Serve with assorted
                    vegetables.""",
                    ingredients='1 cup mayonnaise\r'
                                '1/2 cup tightly packed fresh basil leaves\r'
                                '1 garlic clove, minced\r'
                                '1/2 teaspoon lemon zest\r'
                                '2 teaspoons fresh lemon juice\r'
                                'Pinch of salt\r'
                                'Assorted vegetables',
                    category=category2)
session.add(appetizer2)
session.commit()


category3 = Category(user_id=1, name="quick-meals")
session.add(category3)
session.commit()
quickmeal1 = Recipe(user_id=1,
                    name="Chili-Hash",
                    instructions="""In a microwave-safe dish, with water,
                    cover and microwave potatoes on high until tender -
                    around 7 minutes. While potatoes are cooking, brown beef
                    and  sweat onion; drain. Add drained potatoes to skillet.
                    Stir in peas, chili starter, salt and parsley. Bring to
                    boil. Simmer, uncovered around 5 minutes. Serve with sour
                    cream, optionally.""",
                    ingredients='1 pound medium potatoes, cubed\r'
                                '1/2 cup water\r'
                                '1 pound ground beef\r'
                                '1 medium onion, chopped\r'
                                '1 can (15 1/2 ounces) chili starter\r'
                                '1 cup frozen peas\r'
                                '2 tablespoons minced fresh parsley\r'
                                '1/4 teaspoon salt',
                    category=category3)
session.add(quickmeal1)
session.commit()
quickmeal2 = Recipe(user_id=1,
                    name="Parmesan Garlic Grilled Corn On The Cob",
                    instructions="""Preheat grill to 400F. Melt butter and add
                    cheese, garlic powder, salt, and Italian seasonings. Stir
                    well. Add corn to large piece of foil and pour mixture
                    evenly over the top of the corn. Wrap with more foil so the
                    top is covered. Grill for 30 minutes or until done.""",
                    ingredients='4 ears of corn\r'
                                '1/2 cup Food Lion parmesan cheese, grated\r'
                                '1 teaspoon garlic powder\r'
                                '1/2 cup butter, melted\r'
                                '1/2 teaspoon Food Lion Italian dressing\r'
                                '1/4 teaspoon salt',
                    category=category3)
session.add(quickmeal2)
session.commit()


category4 = Category(user_id=1, name="dinner")
session.add(category4)
session.commit()
dinner1 = Recipe(user_id=1,
                 name="Savory Goulash",
                 instructions="""Brown onion and meat. Add tomato sauce and
                 water. Cook for 2 hours and serve over hot noodles.""",
                 ingredients='2  sliced onions\r'
                             '3 tbsp wesson oil\r'
                             '1 1/2 pounds steak, cubed\r'
                             '3 tsp paprika\r'
                             '1 1/2 tsp salt\r'
                             '1 cup hot water\r'
                             '8 ounces tomato sauce\r'
                             '4 tbsp sour cream\r'
                             'hot buttered noodles\r',
                 category=category4)
session.add(dinner1)
session.commit()

category5 = Category(user_id=1, name="dessert")
session.add(category5)
session.commit()
dessert1 = Recipe(user_id=1, name="Banana Cake",
                  instructions="Bake in three layer pans at 350 degrees.",
                  ingredients='1/2 cup shortening\r'
                               '1 1/2 cups sugar\r'
                               '2 eggs \r'
                               'pinch salt \r'
                               '1/2 cup sour milk\r'
                               '1 tsp soda water\r'
                               '1 3/4 cups flour\r'
                               '1 1/2 tsp baking powder\r'
                               '1/2 cup chopped nuts\r',
                  category=category5)
session.add(dessert1)
session.commit()

dessert2 = Recipe(user_id=1,
                  name="Chocolate Cake",
                  instructions="""Mix all ingredients together.  Pour in 1 cup
                  boiling water.  Mix well.  Bake about 35 minutes at 375
                  degrees.""",
                  ingredients='1/2 cup margarine\r'
                              '2 cups sugar\r'
                              '2  eggs\r'
                              '5 tbsp cocoa\r'
                              '1/2 tsp salt\r'
                              '1/2 cup sour milk\r'
                              '2 tsp baking soda\r'
                              '2 cups flour\r'
                              '1/2 tsp cloves\r'
                              '1 tsp vanilla\r',
                  category=category5)
session.add(dessert2)
session.commit()


category6 = Category(user_id=1, name="lunch")
session.add(category6)
session.commit()
category7 = Category(user_id=1, name="snack")
session.add(category7)
session.commit()
category8 = Category(user_id=1, name="brunch")
session.add(category8)
session.commit()
print("Complete!")

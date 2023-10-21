import sys


class Cookbook:
    def __init__(self) -> None:
        self._cookbook = dict()
        self._cookbook['Sandwich'] = dict(ingredients=list[str](
            ('ham', 'bread', 'cheese', 'tomatoes')), meal='lunch', prep_time=10)
        self._cookbook['Cake'] = dict(
            ingredients=['flour', 'sugar', 'eggs'], meal='dessert', prep_time=60)
        self._cookbook['Salad'] = dict(
            ingredients=['avocado', 'arugula', 'spinach'], meal='lunch', prep_time=15)

    def print_all_recipe_names(self):
        print('Available recipes:')
        for key in self._cookbook.keys():
            print(" - {}" % key)

    def delete_recipe(self, name):
        recipe = self._cookbook.get(name)
        if recipe == None:
            print('Recipe not found.')
            return
        self._cookbook.pop(name)
        print("%s recipe has been deleted." % name)

    def print_recipe_details(self, name):
        recipe = self._cookbook.get(name)
        if recipe == None:
            print('Recipe not found.')
            return
        print("\nRecipe for {}:\n\
        Ingredients list: {}\n\
        To be eaten for {}.\n\
        Takes {} minutes of cooking.\n".format(name, recipe.get('ingredients'), recipe.get('meal'), recipe.get('prep_time')))

    def add_recipe(self):
        name = input('>>> Enter a name:\n')
        print('>>> Enter ingredients:\n')
        listy = []
        while True:
            ing = input()
            if (not ing):
                break
            listy.append(ing)
        meal = input('>>> Enter a meal type:\n')
        time = 0
        while True:
            try:
                time = int(input('>>> Enter a preparation time:\n'))
                break
            except ValueError:
                print('Value not accepted.')
        self._cookbook[name] = dict(
            ingredients=listy, meal=meal, prep_time=time)
        print('%s recipe has been added to cookbook' % name)


def print_usage():
    print('List of available option:\n\
    1: Add a recipe\n\
    2: Delete a recipe\n\
    3: Print a recipe\n\
    4: Print the cookbook\n\
    5: Quit')


def finish():
    print('Cookbook closed. Goodbye !')
    sys.exit(0)


def main():
    print_usage()
    cookbook = Cookbook()
    print('Welcome to the Python Cookbook !')
    while True:
        try:
            print()
            option = int(input('Please select an option:\n>> '))
            if option == 1:
                cookbook.add_recipe()
            elif option == 2:
                cookbook.delete_recipe(
                    input('Please enter the recipe name to be deleted.\n>> '))
            elif option == 3:
                cookbook.print_recipe_details(
                    input('Please enter a recipe name to get its details:\n>> '))
            elif option == 4:
                cookbook.print_all_recipe_names()
            elif option == 5:
                finish()
            else:
                raise ValueError('Unknown option')
        except (KeyboardInterrupt, EOFError):
            finish()
        except ValueError:
            print('Sorry, this option does not exist.')
            print_usage()
        except Exception:
            print('An error occured sorry')
            sys.exit(1)


if __name__ == '__main__':
    main()

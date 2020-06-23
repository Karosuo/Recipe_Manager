def process_recipe_file(file_obj):
    """

    :return:
    """
    pass


def process_plan_file(file_obj):
    """

    :return:
    """
    pass


def process_inventory_file(file_obj):
    """

    :return:
    """
    pass


def generate_shopping_list_from_all(substract_inventory=False):
    """
    Generate a shopping list from all the existing plans
    This will take into consideration all the recipes in those plans, repeated or not, try to add up all the same
    ingredients and group them by Aisle

    :param substract_inventory: bool, determines if the shopping list will include discount what's on the inventory (True) or not (False)
    :return:
    """
    # Get all Profiles
    # Get all the Profile_has_Recipes regs
    # Loop over those regs, on each loop fetch the current recipe ingredients
    # Per each ingredient
    # Check if the ingredient exist on the shopping list
    # if it does not, add it directly
    # if it does exist, check if it has the same MUnit
    # if it has same MUnit, add up the MUnitQty of the new one, to the existing qty on the shopping list
    # if it does not has the same MUnit, find the oldest Ingredient and use its MUnit as base reference
    # if that base unit does not have equivalent qties in the Alternative MUnits, then use the MUnit of the Ingredient
    # of the already added to the shopping list ingredient, if that also does not have equiv, use the new ingredient
    # MUnit as base, if all three fail, add the second ingredient to the shopping list as different ingredient

    # Once the Shopping list is done, go over all the added ingredients, all should be different,e xcept for the cases
    # that the same ingredient had different MUnit without an Alternative one to convert
    # On each loop, check if that ingredient has a Packge and if it has, use the total Qty added to check how many of them
    # are needed as Alternate Qty to show, if the Package and the current loop Ingredient have different MUnits, follow the
    # same logic as before and at the worst case as it's not adding an ingredient but detecting grouping in packages
    # just ignore that package as if the ingredient did not have one since the beginning
    # if the MUnits match, calculate how many Packages are equivalent to the total Qty expected of that Ingredient and
    # save it as Alternative Qty


    pass
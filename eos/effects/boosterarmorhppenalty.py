# boosterArmorHpPenalty
#
# Used by:
# Implants from group: Booster (12 of 47)
type = "boosterSideEffect"
activeByDefault = False


def handler(fit, booster, context):
    fit.ship.boostItemAttr("armorHP", booster.getModifiedItemAttr("boosterArmorHPPenalty"))

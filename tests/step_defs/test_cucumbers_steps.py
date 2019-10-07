import pytest

from pytest_bdd import scenario, parsers, given, when, then

from cucumbers import CucumberBasket

EXTRA_TYPES = {
  'Number': int,
}

CONVERTERS = {
  'initial': int,
  'some': int,
  'total': int,
}

@pytest.mark.parametrize(
  ['initial', 'some', 'total'],
  [(0, 3, 3),
   (2, 4, 6),
   (5, 5,10)])
@scenario('../features/cucumbers.feature', 'Add cucumbers to a basket')
# scenarios('../features/cucumbers.feature', example_converters=CONVERTERS)
def test_add(initial, some, total):
  pass

@given(parsers.cfparse('the basket has "{initial:Number}" cucumbers', extra_types=EXTRA_TYPES))
@given('the basket has "<initial>" cucumbers')
def basket(initial):
  return CucumberBasket(initial_count=initial)


@when(parsers.cfparse('"{some:Number}" cucumbers are added to the basket', extra_types=EXTRA_TYPES))
@when('"<some>" cucumbers are added to the basket')
def add_cucumbers(basket, some):
  basket.add(some)

@when(parsers.cfparse('"{some:Number}" cucumbers are removed from the basket', extra_types=EXTRA_TYPES))
@when('"<some>" cucumbers are removed from the basket')
def remove_cucumbers(basket, some):
  basket.remove(some)

@then(parsers.cfparse('the basket contains "{total:Number}" cucumbers', extra_types=EXTRA_TYPES))
@then('the basket contains "<total>" cucumbers')
def basket_has_total(basket, total):
  assert basket.count == total
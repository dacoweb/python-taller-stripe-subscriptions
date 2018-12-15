import stripe

class TestStripe(object):
    _stripe = False
    _customer_id = False

    def __init__(self, *args, **kwargs):        
        self._stripe = stripe
        self._stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"  # <= enter stripe test key
        self._customer_id = "cus_E9i8RWDSd7vGZZ"  # <= enter customer stripe id for the test

    def create_subscription_plan(self, amount, interval="month", product={"name": "Gold special"}, currency="usd", trial_days=14):
        plan_amt = int(amount * 100)
        plan = self._stripe.Plan.create(
            amount=plan_amt,
            interval=interval,
            product=product,
            currency=currency,            
            trial_period_days=trial_days
        )
        return plan
    
    def get_subscription_plan(self, plan_id):
        plan = self._stripe.Plan.retrieve(plan_id)
        return plan
    
    def get_all_plans(self, limit=5):
        plans = self._stripe.Plan.list(limit=limit)
        return plans
    
    def get_subscription(self, subscription_id):
        self._stripe.Subscription.retrieve(subscription_id)
    
    def get_all_subscription(self, limit=5):
        self._stripe.Subscription.list(limit=limit)

    def create_subscription(self, plan_id, trial_days=14):
        subscription = self._stripe.Subscription.create(
            customer=self._customer_id,
            items=[
                {
                "plan": plan_id,
                },
            ],
            trial_from_plan=True
        )
        # trial_period_days=trial_days  # overwrite subscription plan trial in days
        return subscription

# Testing: 
# from subscription import TestStripe
test = TestStripe()

print("***** List of Subscription Plans: *****")
print(test.get_all_plans())

print("***** List of Subscriptions: *****")
print(test.get_all_subscription())

print("***** Creating a new subscription plan: *****")
subscription_name = "subscription-S001"  # <= change name to another subscription
plan = test.create_subscription_plan(amount=15.95, product={"name": subscription_name})
print(plan)

print("***** Retrieving the subscription plan: *****")
plan_again = test.get_subscription_plan(plan.id)
print(plan_again)

print("***** Creating subscription to customer ******")
print(test.create_subscription(plan.id))
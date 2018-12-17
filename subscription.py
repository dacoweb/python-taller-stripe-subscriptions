import stripe

class TestStripe(object):
    _stripe = False
    _customer_id = False

    def __init__(self, **kwargs):        
        self._stripe = stripe
        self._stripe.api_key = kwargs.get('api_key', "sk_test_4eC39HqLyjWDarjtT1zdp7dc")  # <= enter stripe test key
        self._customer_id = kwargs.get('customer_id', "cus_E9i8RWDSd7vGZZ")  # <= enter customer stripe id for the test

    def create_subscription_plan(self, amount, plan_id, plan_name, product=None, interval="month", currency="usd", trial_days=14):
        plan_amt = int(amount * 100)
        if product:
            # format: product = {"name": "Gold special"}
            plan = self._stripe.Plan.create(
                amount=plan_amt,
                interval=interval,
                product=product,
                currency=currency,
                trial_period_days=trial_days
            )
        else:
            plan = self._stripe.Plan.create(
                amount=plan_amt,
                interval=interval,
                id=plan_id,
                name=plan_name,
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
        subscription = self._stripe.Subscription.retrieve(subscription_id)
        return subscription
    
    def get_all_subscription(self, limit=5):
        subscriptions = self._stripe.Subscription.list(limit=limit)
        return subscriptions

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

    def get_all_subscription_from_plan(self, plan_id):
        subscriptions = self._stripe.Subscription.list(plan=plan_id)
        return subscriptions

    def get_all_webhook_eps(self):        
        endpoints = self._stripe.WebhookEndpoint.list(limit=50)
        return endpoints

# Testing: 
# from subscription import TestStripe
# test = TestStripe()

# print("***** List of Subscription Plans: *****")
# print(test.get_all_plans())

# print("***** List of Subscriptions: *****")
# print(test.get_all_subscription())

# print("***** Creating a new subscription plan: *****")
# plan = test.create_subscription_plan(amount=1.99, plan_id="subscription_unique_id", plan_name="2019 Subscription")
# print(plan)

# print("***** Retrieving the subscription plan: *****")
# plan_again = test.get_subscription_plan(plan.id)
# print(plan_again)

# print("***** Creating subscription to customer ******")
# print(test.create_subscription(plan.id))

# Existing subscriptions on plan:
# print(test.get_all_subscription_from_plan(plan.id))

# Show existing endpoints set:
# print(test.get_all_webhook_eps())
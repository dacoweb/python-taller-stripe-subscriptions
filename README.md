# Workshop Python Creating Stripe Subscription

Create Stripe subscription via python

## Reference

[Stripe API](https://stripe.com/docs/api/subscriptions?lang=python)

## Requirements

- [virtualenv](https://docs.python-guide.org/dev/virtualenvs/)
- [Python library for Stripe’s API](https://pypi.org/project/stripe/)

## Getting Started

Install VirtualEnv:

```
$ pip install virtualenv
```

Create a virtual environment for a project:

```
$ cd my_project_folder
$ virtualenv my_project_env
```

Activate environment:

```
$ source my_project_env/bin/activate
```

Install Stripe dependency:

```
$ pip install stripe
```

Set Stripe test key & Customer ID (subscription.py):

```python
    ....
    def __init__(self, *args, **kwargs):        
        ....
        self._stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"  # <= enter stripe test key
        self._customer_id = "cus_E9i8RWDSd7vGZZ"  # <= enter customer stripe id for the test
    ...
```

On running env, execute:

```
$ python subscription.py
```

Expected result: a new subscription created under the customer id provided.

```
...
***** Creating subscription to customer ******
{
  "application_fee_percent": null,
  "billing": "charge_automatically",
  "billing_cycle_anchor": 1546042950,
  "cancel_at_period_end": false,
  "canceled_at": null,
  "created": 1544833350,
  "current_period_end": 1546042950,
  "current_period_start": 1544833350,
  "customer": "cus_E9i8RWDSd7vGZZ",
  "days_until_due": null,
  "default_source": null,
  "discount": null,
  "ended_at": null,
  "id": "sub_E9kQIt9X7cMU87",
  "items": {
    "data": [
      {
        "created": 1544833350,
        "id": "si_E9kQDNe7DrGOtp",
        "metadata": {},
        "object": "subscription_item",
        "plan": {
          "active": true,
          "aggregate_usage": null,
          "amount": 1595,
          "billing_scheme": "per_unit",
          "created": 1544833348,
          "currency": "usd",
          "id": "plan_E9kQJP3OJUlZdQ",
          "interval": "month",
          "interval_count": 1,
          "livemode": false,
          "metadata": {},
          "nickname": null,
          "object": "plan",
          "product": "prod_E9kQm5trA29eJh",
          "tiers": null,
          "tiers_mode": null,
          "transform_usage": null,
          "trial_period_days": 14,
          "usage_type": "licensed"
        },
        "quantity": 1,
        "subscription": "sub_E9kQIt9X7cMU87"
      }
    ],
    "has_more": false,
    "object": "list",
    "total_count": 1,
    "url": "/v1/subscription_items?subscription=sub_E9kQIt9X7cMU87"
  },
  "livemode": false,
  "metadata": {},
  "object": "subscription",
  "plan": {
    "active": true,
    "aggregate_usage": null,
    "amount": 1595,
    "billing_scheme": "per_unit",
    "created": 1544833348,
    "currency": "usd",
    "id": "plan_E9kQJP3OJUlZdQ",
    "interval": "month",
    "interval_count": 1,
    "livemode": false,
    "metadata": {},
    "nickname": null,
    "object": "plan",
    "product": "prod_E9kQm5trA29eJh",
    "tiers": null,
    "tiers_mode": null,
    "transform_usage": null,
    "trial_period_days": 14,
    "usage_type": "licensed"
  },
  "quantity": 1,
  "start": 1544833350,
  "status": "trialing",
  "tax_percent": null,
  "trial_end": 1546042950,
  "trial_start": 1544833350
}
```

## Maintainer

* **David Castillo** - *Web Developer* - [dacoweb](https://github.com/dacoweb)


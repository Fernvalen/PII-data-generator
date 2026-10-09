from faker import Faker

fake = Faker('en_CA')

def generate_user_profiles(count=10):
    """
    Generate a list of user profiles with fake data.
    Args:
        count (int): The number of user profiles to generate. Default is 10.
    """
    return[{
        "user_id": fake.uuid4(),
        "full_name": fake.name(),
        "email": fake.email(),
        "address": fake.address().replace('\n', ', '),
        "phone_number": fake.phone_number()
    } for _ in range(count)]

def generate_financial_transactions(count=10):
    """
    Generate a list of financial transactions with fake data.
    Args:
        count (int): The number of financial transactions to generate. Default is 10.
    """
    return[{
        "transaction_id": fake.uuid4(),
        "account_number": fake.iban(),
        "transaction_date": fake.date_time_this_year().isoformat(),
        "amount": f"${fake.pydecimal(left_digits=4, right_digits=2, positive=True)}",
        "currency": "CAD",
        "merchant": fake.company(),
    } for _ in range(count)]

def generate_healthcare_records(count=10):
    """
    Generate a list of healthcare records with fake data.
    Args:
        count (int): The number of healthcare records to generate. Default is 10.
    """
    return[{
        "patient_id": fake.uuid4(),
        "patient_name": fake.name(),
        "dob": str(fake.date_of_birth(minimum_age=18, maximum_age=90)),
        "gender": fake.random_element(elements=('Male', 'Female', 'Other')),
        "blood_type": fake.random_element(elements=('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-')),
        "diagnosis": fake.sentence(nb_words=4),
        "treatment": fake.sentence(nb_words=6),
        "prescription": fake.sentence(nb_words=5),
        "provider": fake.company()
    } for _ in range(count)]

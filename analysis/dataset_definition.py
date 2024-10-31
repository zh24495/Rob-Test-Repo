from ehrql import create_dataset
from ehrql.tables.tpp import patients, practice_registrations, medications 

dataset = create_dataset()
dataset.configure_dummy_data(population_size=100)

index_date = "2020-03-31"

has_registration = practice_registrations.for_patient_on(
    index_date
).exists_for_patient()



dataset.define_population(has_registration)

dataset.sex = patients.sex
dataset.date_of_birth = patients.date_of_birth
dataset.number_of_medications=medications.except_where(medications.dmd_code=='39113611000001102').count_for_patient()
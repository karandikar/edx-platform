"""
Models for CME Registration
"""

from django.db import models
from student.models import UserProfile

# Create your models here.


#Fields for CME specific registration page
class CmeUserProfile(UserProfile):
    """
    Object for storing CME Registration information
    Uses multi-table inheritance of UserProfile
    """

    class Meta:
        app_label = 'cme_registration'
        db_table = "cme_registration"

    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    middle_initial = models.CharField(max_length=1, blank=True, null=True)
    birth_date = models.CharField(max_length=5, blank=True, null=True)

    PROFESSIONAL_DESIGNATION_CHOICES = (('AuD', 'AuD'),
                                        ('DDS', 'DDS'),
                                        ('DO', 'DO'),
                                        ('MD', 'MD'),
                                        ('MD,PhD', 'MD,PhD'),
                                        ('MBBS', 'MBBS'),
                                        ('NP', 'NP'),
                                        ('PA', 'PA'),
                                        ('PharmD', 'PharmD'),
                                        ('PhD', 'PhD'),
                                        ('RN', 'RN'),
                                        ('Other', 'Other'),
                                        ('None', 'None'))
    professional_designation = models.CharField(blank=True, null=True, max_length=25, choices=PROFESSIONAL_DESIGNATION_CHOICES)
    license_number = models.CharField(max_length=20, blank=True, null=True, )
    license_country = models.CharField(max_length=50, blank=True, null=True)
    license_state = models.CharField(max_length=50, blank=True, null=True)

    PHYSICIAN_STATUS_CHOICES = (('Active', 'Active'),
                                ('Resident', 'Resident'),
                                ('Fellow', 'Fellow'),
                                ('Retired', 'Retired'))
    physician_status = models.CharField(blank=True, null=True, max_length=8, choices=PHYSICIAN_STATUS_CHOICES)

    PATIENT_POPULATION_CHOICES = (('Adult', 'Adult'),
                                  ('Pediatric', 'Pediatric'),
                                  ('Both', 'Both'),
                                  ('None', 'None'))
    patient_population = models.CharField(blank=True, null=True, max_length=25, choices=PATIENT_POPULATION_CHOICES)

    SPECIALTY_CHOICES = (('Addiction_Medicine', 'Addiction Medicine'),
                         ('Adolescent_Medicine', 'Adolescent Medicine'),
                         ('Allergy', 'Allergy'),
                         ('Anesthesiology', 'Anesthesiology'),
                         ('Cardiology', 'Cardiology'),
                         ('Complimentary_Medicine', 'Complimentary Medicine'),
                         ('Critical_Care_Medicine_&_ICU', 'Critical Care Medicine & ICU'),
                         ('Dentistry', 'Dentistry'),
                         ('Dermatology', 'Dermatology'),
                         ('Emergency_Medicine', 'Emergency Medicine'),
                         ('Endocrinology', 'Endocrinology'),
                         ('Family_Practice', 'Family Practice'),
                         ('Gastroenterology_&_Hepatology', 'Gastroenterology & Hepatology'),
                         ('General_Practice', 'General Practice'),
                         ('Gerontology', 'Gerontology'),
                         ('Head_&_Neck_Surgery', 'Head & Neck Surgery'),
                         ('Health_Education', 'Health Education'),
                         ('Hematology', 'Hematology'),
                         ('Immunology_&_Rheumatology', 'Immunology & Rheumatology'),
                         ('Infectious_Disease', 'Infectious Disease'),
                         ('Internal_Medicine', 'Internal Medicine'),
                         ('Neonatology', 'Neonatology'),
                         ('Nephrology', 'Nephrology'),
                         ('Neurology', 'Neurology'),
                         ('Neurosurgery', 'Neurosurgery'),
                         ('Nutrition', 'Nutrition'),
                         ('Obstetrics_&_Gynecology', 'Obstetrics & Gynecology'),
                         ('Oncology', 'Oncology'),
                         ('Ophthalmology', 'Ophthalmology'),
                         ('Orthopaedic_Surgery', 'Orthopaedic Surgery'),
                         ('Palliative_Care', 'Palliative Care'),
                         ('Pathology', 'Pathology'),
                         ('Pediatrics', 'Pediatrics'),
                         ('Pharmacology', 'Pharmacology'),
                         ('Physical_Medicine_&_Rehabilitation', 'Physical Medicine & Rehabilitation'),
                         ('Psychiatry', 'Psychiatry'),
                         ('Psychology', 'Psychology'),
                         ('Public_Health', 'Public Health'),
                         ('Pulmonology', 'Pulmonology'),
                         ('Radiation_Oncology', 'Radiation Oncology'),
                         ('Radiology', 'Radiology'),
                         ('Surgery', 'Surgery'),
                         ('Transplant', 'Transplant'),
                         ('Urology', 'Urology'))

    specialty = models.CharField(blank=True, null=True, max_length=255, choices=SPECIALTY_CHOICES)
    sub_specialty = models.CharField(blank=True, null=True, max_length=255)

    AFFILIATION_CHOICES = (('Stanford Children\'s Health', 'Stanford Children\'s Health'),
                           ('Packard Children\'s Health Alliance (PCHA)', 'Packard Children\'s Health Alliance (PCHA)'),
                           ('Stanford Health Care', 'Stanford Health Care'),
                           ('Stanford University', 'Stanford University'),
                           ('University Healthcare Alliance (UHA)', 'University Healthcare Alliance (UHA)'),
                           ('Not affiliated with Stanford Medicine', 'Not affiliated with Stanford Medicine'),
                           )
    affiliation = models.CharField(blank=True, null=True, max_length=46, choices=AFFILIATION_CHOICES)
    other_affiliation = models.CharField(blank=True, null=True, max_length=46)
    sub_affiliation = models.CharField(blank=True, null=True, max_length=46)

    DEPARTMENT_CHOICES = (('Anesthesiology,Perioperative,Pain Medicine', 'Anesthesiology,Perioperative,Pain Medicine'),
                          ('Biochemistry', 'Biochemistry'),
                          ('Cardiothoracic Surgery', 'Cardiothoracic Surgery'),
                          ('Centers - School of Medicine', 'Centers - School of Medicine'),
                          ('Chemical and Systems Biology', 'Chemical and Systems Biology'),
                          ('Comparative Medicine', 'Comparative Medicine'),
                          ('Dermatology', 'Dermatology'),
                          ('Developmental Biology', 'Developmental Biology'),
                          ('Genetics Operations', 'Genetics Operations'),
                          ('Health Research and Policy', 'Health Research and Policy'),
                          ('Medicine', 'Medicine'),
                          ('Microbiology and Immunology', 'Microbiology and Immunology'),
                          ('Molecular and Cellular Physiology', 'Molecular and Cellular Physiology'),
                          ('Neurobiology', 'Neurobiology'),
                          ('Neurology', 'Neurology'),
                          ('Neurosurgery', 'Neurosurgery'),
                          ('Obstetrics & Gynecology', 'Obstetrics & Gynecology'),
                          ('Ophthalmology', 'Ophthalmology'),
                          ('Orthopaedic Surgery', 'Orthopaedic Surgery'),
                          ('Otolaryngology/Head & Neck Surgery', 'Otolaryngology/Head & Neck Surgery'),
                          ('Pathology', 'Pathology'),
                          ('Pediatrics', 'Pediatrics'),
                          ('Psychiatry and Behavioral Sciences', 'Psychiatry and Behavioral Sciences'),
                          ('Radiation Oncology', 'Radiation Oncology'),
                          ('Radiology', 'Radiology'),
                          ('School of Medicine', 'School of Medicine'),
                          ('SoM - Basic Science Pool', 'SoM - Basic Science Pool'),
                          ('SoM - Bio-X/Clark', 'SoM - Bio-X/Clark'),
                          ('SoM - Bioengineering', 'SoM - Bioengineering'),
                          ('SoM - Clinical Science Pool', 'SoM - Clinical Science Pool'),
                          ('SoM - Other Departments', 'SoM - Other Departments'),
                          ('SoM Dean\'s Office Administrative Units', 'SoM Dean\'s Office Administrative Units'),
                          ('SoM Non Cap Projects', 'SoM Non Cap Projects'),
                          ('Stanford Cancer/Stem Cell Biology', 'Stanford Cancer/Stem Cell Biology'),
                          ('Stanford Institutes of Medicine', 'Stanford Institutes of Medicine'),
                          ('Structural Biology Department', 'Structural Biology Department'),
                          ('Surgery', 'Surgery'),
                          ('Urology', 'Urology'),
                          ('Urology - Administration', 'Urology - Administration'),
                          ('Urology - Divisions', 'Urology - Divisions'))
    stanford_department = models.CharField(blank=True, null=True, max_length=46, choices=DEPARTMENT_CHOICES)
    sunet_id = models.CharField(blank=True, null=True, max_length=33)

    address_1 = models.TextField(blank=True, null=True)
    address_2 = models.TextField(blank=True, null=True)
    city_cme = models.TextField(blank=True, null=True)
    STATE_CHOICES = (('AL', 'Alabama'),
                     ('AK', 'Alaska'),
                     ('AZ', 'Arizona'),
                     ('AR', 'Arkansas'),
                     ('CA', 'California'),
                     ('CO', 'Colorado'),
                     ('CT', 'Connecticut'),
                     ('DE', 'Deleware'),
                     ('DC', 'District of Columbia'),
                     ('FL', 'Florida'),
                     ('GA', 'Georgia'),
                     ('HI', 'Hawaii'),
                     ('ID', 'Idaho'),
                     ('IL', 'Illinois'),
                     ('IN', 'Indiana'),
                     ('IA', 'Iowa'),
                     ('KS', 'Kansas'),
                     ('KY', 'Kentucky'),
                     ('LA', 'Louisiana'),
                     ('ME', 'Maine'),
                     ('MD', 'Maryland'),
                     ('MA', 'Massachusetts'),
                     ('MI', 'Michigan'),
                     ('MN', 'Minnesota'),
                     ('MS', 'Mississippi'),
                     ('MO', 'Missouri'),
                     ('MT', 'Montana'),
                     ('NE', 'Nebraska'),
                     ('NV', 'Nevada'),
                     ('NH', 'New Hampshire'),
                     ('NJ', 'New Jersey'),
                     ('NM', 'New Mexico'),
                     ('NY', 'New York'),
                     ('NC', 'North Carolina'),
                     ('ND', 'North Dakota'),
                     ('OH', 'Ohio'),
                     ('OK', 'Oklahoma'),
                     ('OR', 'Oregon'),
                     ('PA', 'Pennsylvania'),
                     ('RI', 'Rhode Island'),
                     ('SC', 'South Carolina'),
                     ('SD', 'South Dakota'),
                     ('TN', 'Tennessee'),
                     ('TX', 'Texas'),
                     ('UT', 'Utah'),
                     ('VT', 'Vermont'),
                     ('VA', 'Virginia'),
                     ('WA', 'Washington'),
                     ('WV', 'West Virginia'),
                     ('WI', 'Wisconsin'),
                     ('WY', 'Wyoming'))

    state = models.CharField(blank=True, null=True, max_length=50, choices=STATE_CHOICES)
    county_province = models.CharField(blank=True, null=True, max_length=50)
    postal_code = models.CharField(blank=True, null=True, max_length=20)
    COUNTRY_CHOICES = (('United States', 'United States'),
                       ('Afghanistan', 'Afghanistan'),
                       ('Aland Islands', 'Aland Islands'),
                       ('Albania', 'Albania'),
                       ('Algeria', 'Algeria'),
                       ('American Samoa', 'American Samoa'),
                       ('Andorra', 'Andorra'),
                       ('Angola', 'Angola'),
                       ('Anguilla', 'Anguilla'),
                       ('Antarctica', 'Antarctica'),
                       ('Antigua And Barbuda', 'Antigua And Barbuda'),
                       ('Argentina', 'Argentina'),
                       ('Armenia', 'Armenia'),
                       ('Aruba', 'Aruba'),
                       ('Australia', 'Australia'),
                       ('Austria', 'Austria'),
                       ('Azerbaijan', 'Azerbaijan'),
                       ('Bahamas', 'Bahamas'),
                       ('Bahrain', 'Bahrain'),
                       ('Bangladesh', 'Bangladesh'),
                       ('Barbados', 'Barbados'),
                       ('Belarus', 'Belarus'),
                       ('Belgium', 'Belgium'),
                       ('Belize', 'Belize'),
                       ('Benin', 'Benin'),
                       ('Bermuda', 'Bermuda'),
                       ('Bhutan', 'Bhutan'),
                       ('Bolivia', 'Bolivia'),
                       ('Bosnia And Herzegovina', 'Bosnia And Herzegovina'),
                       ('Botswana', 'Botswana'),
                       ('Bouvet Island', 'Bouvet Island'),
                       ('Brazil', 'Brazil'),
                       ('British Indian Ocean Territory', 'British Indian Ocean Territory'),
                       ('Brunei Darussalam', 'Brunei Darussalam'),
                       ('Bulgaria', 'Bulgaria'),
                       ('Burkina Faso', 'Burkina Faso'),
                       ('Burundi', 'Burundi'),
                       ('Cambodia', 'Cambodia'),
                       ('Cameroon', 'Cameroon'),
                       ('Canada', 'Canada'),
                       ('Cape Verde', 'Cape Verde'),
                       ('Cayman Islands', 'Cayman Islands'),
                       ('Central African Republic', 'Central African Republic'),
                       ('Chad', 'Chad'),
                       ('Chile', 'Chile'),
                       ('China', 'China'),
                       ('Christmas Island', 'Christmas Island'),
                       ('Cocos (Keeling) Islands', 'Cocos (Keeling) Islands'),
                       ('Colombia', 'Colombia'),
                       ('Comoros', 'Comoros'),
                       ('Congo', 'Congo'),
                       ('Congo, The Democratic Republic OfThe', 'Congo, The Democratic Republic OfThe'),
                       ('Cook Islands', 'Cook Islands'),
                       ('Costa Rica', 'Costa Rica'),
                       ('Cote D\'lvoire', 'Cote D\'lvoire'),
                       ('Croatia', 'Croatia'),
                       ('Cuba', 'Cuba'),
                       ('Cyprus', 'Cyprus'),
                       ('Czech Republic', 'Czech Republic'),
                       ('Denmark', 'Denmark'),
                       ('Djibouti', 'Djibouti'),
                       ('Dominica', 'Dominica'),
                       ('Dominican Republic', 'Dominican Republic'),
                       ('Ecuador', 'Ecuador'),
                       ('Egypt', 'Egypt'),
                       ('El Salvador', 'El Salvador'),
                       ('Equatorial Guinea', 'Equatorial Guinea'),
                       ('Eritrea', 'Eritrea'),
                       ('Estonia', 'Estonia'),
                       ('Ethiopia', 'Ethiopia'),
                       ('Falkland Islands (Malvinas)', 'Falkland Islands (Malvinas)'),
                       ('Faroe Islands', 'Faroe Islands'),
                       ('Fiji', 'Fiji'),
                       ('Finland', 'Finland'),
                       ('France', 'France'),
                       ('French Guiana', 'French Guiana'),
                       ('French Polynesia', 'French Polynesia'),
                       ('French Southern Territories', 'French Southern Territories'),
                       ('Gabon', 'Gabon'),
                       ('Gambia', 'Gambia'),
                       ('Georgia', 'Georgia'),
                       ('Germany', 'Germany'),
                       ('Ghana', 'Ghana'),
                       ('Gibraltar', 'Gibraltar'),
                       ('Greece', 'Greece'),
                       ('Greenland', 'Greenland'),
                       ('Grenada', 'Grenada'),
                       ('Guadeloupe', 'Guadeloupe'),
                       ('Guam', 'Guam'),
                       ('Guatemala', 'Guatemala'),
                       ('Guernsey', 'Guernsey'),
                       ('Guinea', 'Guinea'),
                       ('Guinea-Bissau', 'Guinea-Bissau'),
                       ('Guyana', 'Guyana'),
                       ('Haiti', 'Haiti'),
                       ('Heard Island And McDonald Is lands', 'Heard Island And McDonald Is lands'),
                       ('Holy See (Vatican City State)', 'Holy See (Vatican City State)'),
                       ('Honduras', 'Honduras'),
                       ('Hong Kong', 'Hong Kong'),
                       ('Hungary', 'Hungary'),
                       ('Iceland', 'Iceland'),
                       ('India', 'India'),
                       ('Indonesia', 'Indonesia'),
                       ('Iran, Islamic Republic Of', 'Iran, Islamic Republic Of'),
                       ('Iraq', 'Iraq'),
                       ('Ireland', 'Ireland'),
                       ('Isle Of Man', 'Isle Of Man'),
                       ('Israel', 'Israel'),
                       ('Italy', 'Italy'),
                       ('Jamaica', 'Jamaica'),
                       ('Japan', 'Japan'),
                       ('Jersey', 'Jersey'),
                       ('Jordan', 'Jordan'),
                       ('Kazakhstan', 'Kazakhstan'),
                       ('Kenya', 'Kenya'),
                       ('Kiribati', 'Kiribati'),
                       ('Korea, Democratic People\'s Republic Of', 'Korea, Democratic People\'s Republic Of'),
                       ('Korea, Republic Of', 'Korea, Republic Of'),
                       ('Kuwait', 'Kuwait'),
                       ('Kyrgyzstan', 'Kyrgyzstan'),
                       ('Lao People\'s Democratic Republic', 'Lao People\'s Democratic Republic'),
                       ('Latvia', 'Latvia'),
                       ('Lebanon', 'Lebanon'),
                       ('Lesotho', 'Lesotho'),
                       ('Liberia', 'Liberia'),
                       ('Libyan Arab Jamahiriya', 'Libyan Arab Jamahiriya'),
                       ('Liechtenstein', 'Liechtenstein'),
                       ('Lithuania', 'Lithuania'),
                       ('Luxembourg', 'Luxembourg'),
                       ('Macao', 'Macao'),
                       ('Macedonia, The Former Yugoslav Republic Of', 'Macedonia, The Former Yugoslav Republic Of'),
                       ('Madagascar', 'Madagascar'),
                       ('Malawi', 'Malawi'),
                       ('Malaysia', 'Malaysia'),
                       ('Maldives', 'Maldives'),
                       ('Mali', 'Mali'),
                       ('Malta', 'Malta'),
                       ('Marshall Islands', 'Marshall Islands'),
                       ('Martinique', 'Martinique'),
                       ('Mauritania', 'Mauritania'),
                       ('Mauritius', 'Mauritius'),
                       ('Mayotte', 'Mayotte'),
                       ('Mexico', 'Mexico'),
                       ('Micronesia, Federated States Of', 'Micronesia, Federated States Of'),
                       ('Moldova, Republic Of', 'Moldova, Republic Of'),
                       ('Monaco', 'Monaco'),
                       ('Mongolia', 'Mongolia'),
                       ('Montenegro', 'Montenegro'),
                       ('Montserrat', 'Montserrat'),
                       ('Morocco', 'Morocco'),
                       ('Mozambique', 'Mozambique'),
                       ('Myanmar', 'Myanmar'),
                       ('Namibia', 'Namibia'),
                       ('Nauru', 'Nauru'),
                       ('Nepal', 'Nepal'),
                       ('Netherlands', 'Netherlands'),
                       ('Netherlands Antilles', 'Netherlands Antilles'),
                       ('New Caledonia', 'New Caledonia'),
                       ('New Zealand', 'New Zealand'),
                       ('Nicaragua', 'Nicaragua'),
                       ('Niger', 'Niger'),
                       ('Nigeria', 'Nigeria'),
                       ('Niue', 'Niue'),
                       ('Norfolk Island', 'Norfolk Island'),
                       ('Northern Mariana Islands', 'Northern Mariana Islands'),
                       ('Norway', 'Norway'),
                       ('Oman', 'Oman'),
                       ('Pakistan', 'Pakistan'),
                       ('Palau', 'Palau'),
                       ('Palestinian Territory, Occupied', 'Palestinian Territory, Occupied'),
                       ('Panama', 'Panama'),
                       ('Papua New Guinea', 'Papua New Guinea'),
                       ('Paraguay', 'Paraguay'),
                       ('Peru', 'Peru'),
                       ('Philippines', 'Philippines'),
                       ('Pitcairn', 'Pitcairn'),
                       ('Poland', 'Poland'),
                       ('Portugal', 'Portugal'),
                       ('Puerto Rico', 'Puerto Rico'),
                       ('Qatar', 'Qatar'),
                       ('Reunion', 'Reunion'),
                       ('Romania', 'Romania'),
                       ('Russia', 'Russia'),
                       ('Rwanda', 'Rwanda'),
                       ('Saint Helena', 'Saint Helena'),
                       ('Saint Kitts And Nevis', 'Saint Kitts And Nevis'),
                       ('Saint Lucia', 'Saint Lucia'),
                       ('Saint Pierre And Miquelon', 'Saint Pierre And Miquelon'),
                       ('Saint Vincent And The Grenadines', 'Saint Vincent And The Grenadines'),
                       ('Samoa', 'Samoa'),
                       ('San Marino', 'San Marino'),
                       ('Sao Tome And Principe', 'Sao Tome And Principe'),
                       ('Saudi Arabia', 'Saudi Arabia'),
                       ('Senegal', 'Senegal'),
                       ('Serbia', 'Serbia'),
                       ('Seychelles', 'Seychelles'),
                       ('Sierra Leone', 'Sierra Leone'),
                       ('Singapore', 'Singapore'),
                       ('Slovakia', 'Slovakia'),
                       ('Slovenia', 'Slovenia'),
                       ('Solomon Islands', 'Solomon Islands'),
                       ('Somalia', 'Somalia'),
                       ('South Africa', 'South Africa'),
                       ('South Georgia And The South Sandwich Islands', 'South Georgia And The South Sandwich Islands'),
                       ('South Sudan', 'South Sudan'),
                       ('Spain', 'Spain'),
                       ('Sri Lanka', 'Sri Lanka'),
                       ('Sudan', 'Sudan'),
                       ('Suriname', 'Suriname'),
                       ('Svalbard And Jan Mayen', 'Svalbard And Jan Mayen'),
                       ('Swaziland', 'Swaziland'),
                       ('Sweden', 'Sweden'),
                       ('Switzerland', 'Switzerland'),
                       ('Syrian Arab Republic', 'Syrian Arab Republic'),
                       ('Taiwan', 'Taiwan'),
                       ('Tajikistan', 'Tajikistan'),
                       ('Tanzania, United Republic Of', 'Tanzania, United Republic Of'),
                       ('Thailand', 'Thailand'),
                       ('Timor-Leste', 'Timor-Leste'),
                       ('Togo', 'Togo'),
                       ('Tokelau', 'Tokelau'),
                       ('Tonga', 'Tonga'),
                       ('Trinidad And Tobago', 'Trinidad And Tobago'),
                       ('Tunisia', 'Tunisia'),
                       ('Turkey', 'Turkey'),
                       ('Turkmenistan', 'Turkmenistan'),
                       ('Turks And Caicos Islands', 'Turks And Caicos Islands'),
                       ('Tuvalu', 'Tuvalu'),
                       ('U.S. Minor Outlying Islands', 'U.S. Minor Outlying Islands'),
                       ('Uganda', 'Uganda'),
                       ('Ukraine', 'Ukraine'),
                       ('United Arab Emirates', 'United Arab Emirates'),
                       ('United Kingdom', 'United Kingdom'),
                       ('Uruguay', 'Uruguay'),
                       ('Uzbekistan', 'Uzbekistan'),
                       ('Vanuatu', 'Vanuatu'),
                       ('Venezuela', 'Venezuela'),
                       ('Viet Nam', 'Viet Nam'),
                       ('Virgin Islands, British', 'Virgin Islands, British'),
                       ('Virgin Islands, U.S.', 'Virgin Islands, U.S.'),
                       ('Wallis And Futuna', 'Wallis And Futuna'),
                       ('Western Sahara', 'Western Sahara'),
                       ('Yemen', 'Yemen'),
                       ('Zambia', 'Zambia'),
                       ('Zimbabwe', 'Zimbabwe'),
                       ('Other', 'Other'))

    country_cme = models.CharField(blank=True, null=True, max_length=50, choices=COUNTRY_CHOICES)
    GENDER_CHOICES = (('m', 'Male'),
                      ('f', 'Female'))

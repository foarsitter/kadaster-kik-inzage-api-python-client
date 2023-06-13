datamodel-codegen \
--url https://developer.kadaster.nl/schemas/kik-inzage/6.0.x/openapi.yaml \
--output ./src/kikinzage/models/generated.py \
--target-python-version 3.8 \
--snake-case-field \
--capitalise-enum-members \
--input-file-type openapi \
--field-constraints
#--collapse-root-model

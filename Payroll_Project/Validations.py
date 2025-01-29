from abc import ABC, abstractmethod

class Validator(ABC):
    @abstractmethod
    def is_valid(self):
        pass

class StructureValidator(Validator):
    def is_valid(self):
        print("The Structure Validator is Valid")
        return True

class CoreFieldsValidator(Validator):
    def is_valid(self):
        print("The Core Field Validator is Valid")
        return True

class SignatureValidator(Validator):
    def is_valid(self):
        print("The Signature Validator is Valid")
        return True

class NationalIDValidator(Validator):
    def is_valid(self):
        print("The National ID Validator is Valid")
        return True

class TaxpayerValidator(Validator):
    def is_valid(self):
        print("The Taxpayer ID Validator is Valid")
        return True

class ReferenceDocumentValidator(Validator):
    def is_valid(self):
        print("The Reference Document ID Validator is Valid")
        return True

class CodeValidator(Validator):
    def is_valid(self):
        print("The Code Document ID Validator is Valid")
        return True

class SimpleFieldsValidator(Validator):
    def is_valid(self):
        print("The Simple Field Document ID Validator is Valid")
        return True

class ValidatorGroup:
    def __init__(self, validators):
        self.validators = validators

    def validate(self):
        for validator in self.validators:
            if not validator.is_valid():
                return False
        return True

class DocumentValidation:
    def __init__(self, validator_group):
        self.validator_group = validator_group

    def is_validate(self):
        if self.validator_group.validate():
            return "ALL the Validation Process is True"
        return "Validation Failed"

    
if __name__ == "__main__":
    structure_validator = StructureValidator()
    core_validator = CoreFieldsValidator()
    signature_validator = SignatureValidator()
    national_validator = NationalIDValidator()
    taxpayer_validator = TaxpayerValidator()
    reference_validator = ReferenceDocumentValidator()
    code_validator = CodeValidator()
    simple_validator = SimpleFieldsValidator()

    mandatory_validators = ValidatorGroup([structure_validator, core_validator, signature_validator])
    complete_validators = ValidatorGroup([
        structure_validator, core_validator, signature_validator,
        national_validator, taxpayer_validator, reference_validator,
        code_validator, simple_validator
    ])

    print("Mandatory Validation:")
    doc_mandatory = DocumentValidation(mandatory_validators)
    print(doc_mandatory.is_validate())

    print("\nComplete Validation:")
    doc_complete = DocumentValidation(complete_validators)
    print(doc_complete.is_validate())
import shortuuid


class OAuthConstants:

    """Generates the keys for the application
    """

    @staticmethod
    def generate_application_key():
        """Generate the application key

        Returns:
            str: the key
        """
        return shortuuid.ShortUUID().random(length=32)

    @staticmethod
    def generate_application_secret():
        """Generate the application secret

        Returns:
            str: the secret
        """
        return shortuuid.ShortUUID().random(length=64)

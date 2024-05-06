from flask import current_app


def get_aws_credentials():
    return {
        'aws_access_key_id': current_app.config.get('AWS_ACCESS_KEY_ID'),
        'aws_secret_access_key': current_app.config.get('AWS_SECRET_ACCESS_KEY'),
        'region_name': current_app.config.get('AWS_REGION')
    }

# products/utils.py

def get_resized_image_url(image_field, width=800, height=800):
    if image_field and hasattr(image_field, 'url'):
        original_url = image_field.url
        return original_url.replace(
            '/upload/',
            f'/upload/w_{width},h_{height},c_limit,q_auto/'
        )
    return None

def build_prompt(provider: str, region: str, resource_type: str, resource_name: str, attributes: dict) -> str:
    return f"""
    You are an expert Terraform developer.
    Generate a Terraform HCL resource script based on the provided JSON attributes.

    Instructions:
    1.  **Validate**: Confirm `{resource_type}` is a valid resource for the `{provider}` provider.
    2.  **Use Valid Attributes**: Only include attributes recognized by the Terraform Registry for this resource type.
    3.  **Use Defaults**: If an attribute is optional and not provided in the input, use an appropriate default value.
    4.  **Add Tags**: Include a `tags` block with at least one key-value pair, such as `Name = "{resource_name}"`.
    5.  **Set Region**: Use `{region}` as the provider region.
    6.  **Return Format**: Provide only the raw Terraform HCL code block. Do not include any Markdown formatting, explanations, or additional text.

    Example 1:
    resource "aws_s3_bucket" "example" {{
    bucket = "my-example-bucket"
    acl    = "private"
    tags = {{
        Name        = "my-example-bucket"
        Environment = "generated-by-ai"
    }}
    }}

    Example 2:
    resource "aws_instance" "web" {{
    ami           = "ami-0c55b159cbfafe1f0"
    instance_type = "t2.micro"
    tags = {{
        Name = "web"
    }}
    }}

    Input:
    Provider: {provider}
    Region: {region}
    Resource type: {resource_type}
    Resource name: {resource_name}
    Attributes: {attributes}
    """

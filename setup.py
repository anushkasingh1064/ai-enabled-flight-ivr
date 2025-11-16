from setuptools import setup, find_packages

setup(
    name="indian-airlines-ivr",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.104.1",
        "uvicorn[standard]==0.24.0",
        "twilio==8.10.0",
        "redis==5.0.1",
        "openai==1.3.0",
        "python-dotenv==1.0.0",
        "pydantic==2.5.0",
        "python-multipart==0.0.6",
    ],
    python_requires=">=3.8",
)
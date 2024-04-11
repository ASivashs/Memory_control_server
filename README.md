# Memory usage server

This server app provide you ability to upload and store data about RAM and ROM in your system. Also you can store data from [Memory_control_scripts](https://github.com/ASivashs/Memory_usage_scripts). 


## Requirements

This app tested with following versions of required programs:

- Python 3.11.9 > 
- Docker 26 > 
- Docker compose v2.25.0


## Installation & Running

1. Clone the repository:
```
git clone https://github.com/ASivashs/Memory_usage_scripts.git
```

2. Running:
```
docker compose up
```


## Usage

You can send GET, GET (with id), POST, PUT requests to this app. To start working with app you should do request to http://127.0.0.1:8080/reports.

In this app you can store data in JSON format in NoSQL database MongoDB. Example of JSON:
```
{
  "total": "13824",
  "used": "11059",
  "used_percentage": 80,
  "free": "526",
  "shared": "350",
  "cache": "2914"
}
```





# Memory Usage Server

The Memory Usage Server provides you with the ability to upload and store data about RAM and ROM in your system. Additionally, you can store data from the [Memory Control Scripts](https://github.com/ASivashs/Memory_usage_scripts).

## Requirements

This app has been tested with the following versions of required programs:

- **Python 3.11.9**
- **Docker 26**
- **Docker Compose v2.25.0**

## Installation & Running

1. Clone the repository:
    ```bash
    git clone https://github.com/ASivashs/Memory_usage_scripts.git
    ```

2. Run the server:
    ```bash
    docker compose up
    ```

## Usage

You can send **GET**, **GET (with ID)**, **POST**, and **PUT** requests to this app. To start working with the app, make requests to `http://127.0.0.1:8080/reports`.

In this app, you can store data in JSON format in the NoSQL database MongoDB. Here's an example of a JSON data entry:

```json
{
  "total": "13824",
  "used": "11059",
  "used_percentage": 80,
  "free": "526",
  "shared": "350",
  "cache": "2914"
}
```
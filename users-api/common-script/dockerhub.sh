get_docker_image_latest_version() {
  local repository=$1           # имя репозитория (например, users-api)
  local user=$2                 # логин в DockerHub
  local password=$3             # токен (или пароль) DockerHub

  # Авторизация и получение токена
  response=$(curl -s -H "Content-Type: application/json" \
      -X POST -d "{\"username\": \"${user}\", \"password\": \"${password}\"}" \
      https://hub.docker.com/v2/users/login/)

  token=$(echo $response | jq -r .token)

  if [ "$token" == "null" ]; then
    echo "Login failed"
    exit 1
  else
    echo "Login successful"
  fi

  # Получение тэгов (версий) образа
  response=$(curl -s -H "Authorization: Bearer $token" \
      "https://hub.docker.com/v2/repositories/${user}/${repository}/tags")

  # Получение самого свежего тега (по дате обновления)
  latest_name=$(echo "$response" | jq -r '.results | map(select(.content_type == "image")) | max_by(.last_updated) | .name')

  echo "$latest_name"
}

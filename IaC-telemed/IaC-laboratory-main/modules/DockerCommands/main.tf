resource "null_resource" "docker_commands" {
  provisioner "local-exec" {
    command = "docker tag unal-telemed-main us-east4-docker.pkg.dev/cbse-2024ii-438603/unal-telemed-main/unal-telemed-main"
  }

  provisioner "local-exec" {
    command = "docker push us-east4-docker.pkg.dev/cbse-2024ii-438603/unal-telemed-main/unal-telemed-main"
  }
}
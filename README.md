Este es un proyecto simple que demuestra cómo usar la biblioteca cryptography de Python para cifrar y descifrar mensajes utilizando el algoritmo Fernet. Fernet es una especificación de cifrado simétrico que garantiza que los mensajes cifrados no pueden ser alterados o leídos sin la clave.


  // Paso 1: Generar una clave de cifrado
  // La clave es como la contraseña, se usa para encriptar y desencriptar.
  CLAVE = GENERAR_CLAVE_FERNET()
  
  // Paso 2: Crear el objeto de cifrado
  // Usamos la clave para crear la herramienta que realizará el trabajo.
  OBJETO_CIFRADO = CREAR_OBJETO_FERNET(CLAVE)
  
  // Paso 3: Preparar el mensaje original
  // El mensaje debe estar en formato de "bytes", por eso la 'b'.
  MENSAJE_ORIGINAL = "Este es un mensaje secreto."
  MENSAJE_EN_BYTES = CONVERTIR_A_BYTES(MENSAJE_ORIGINAL)
  
  // Paso 4: Cifrar el mensaje
  // Usamos el objeto de cifrado para encriptar el mensaje en bytes.
  MENSAJE_CIFRADO = OBJETO_CIFRADO.CIFRAR(MENSAJE_EN_BYTES)
  
  // Paso 5: Mostrar el resultado
  IMPRIMIR("Mensaje cifrado:", MENSAJE_CIFRADO)
  
  // Paso 6: Descifrar el mensaje
  // Usamos el mismo objeto de cifrado y la misma clave para descifrarlo.
  MENSAJE_DESCIFRADO_EN_BYTES = OBJETO_CIFRADO.DESCIFRAR(MENSAJE_CIFRADO)
  
  // Paso 7: Convertir el mensaje de vuelta a texto
  // El resultado del descifrado también es en bytes, lo convertimos a texto legible.
  MENSAJE_DESCIFRADO_FINAL = CONVERTIR_A_TEXTO(MENSAJE_DESCIFRADO_EN_BYTES)
  
  // Paso 8: Mostrar el resultado final
  IMPRIMIR("Mensaje descifrado:", MENSAJE_DESCIFRADO_FINAL)

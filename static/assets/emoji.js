window.onload = función() {    
//     Establece el tamaño de los Emojis renderizados   
//     Esto se puede establecer en 16x16, 36x36 o 72x72   
   twemoji.size = '16x16';    
    // Analizar el cuerpo del documento y   
    // insertar <img> etiquetas en lugar de Unicode Emojis   
    twemoji.parse(document.body);    
} 
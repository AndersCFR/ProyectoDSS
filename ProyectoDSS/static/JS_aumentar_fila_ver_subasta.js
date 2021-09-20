function agregarFila(){
    document.getElementById("tablaprueba").insertRow(-1).innerHTML = '<td></td><td></td><td></td><td><button>Finalizar</button></td>';
  }
  
  function eliminarFila(){
    var table = document.getElementById("tablaprueba");
    var rowCount = table.rows.length;
    //console.log(rowCount);
    
    if(rowCount <= 1)
      alert('No se puede eliminar el encabezado');
    else
      table.deleteRow(rowCount -1);
  }
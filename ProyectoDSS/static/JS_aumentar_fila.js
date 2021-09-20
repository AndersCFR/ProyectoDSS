function agregarFila(){
    document.getElementById("tablaprueba").insertRow(-1).innerHTML = '<td><input></td><td><input></td><td><input></td>';
  }
  
  function eliminarFila(){
    //alert('Heyy');
    var table = document.getElementById("tablaprueba");
    var rowCount = table.rows.length;
    //console.log(rowCount);
    
    if(rowCount <= 1)
      alert('No se puede eliminar el encabezado');
    else
      table.deleteRow(rowCount -1);
  }
var print_column = gridIncassi.columns.find(function (v, i) {
    return gridIncassi.columns[i].field === "stampa_reso";
});
var lista_negozi = $(.element-lista_negozi select).val();
if(lista_negozi != null){
    gridIncassi.showColumn(print_column.field);
}

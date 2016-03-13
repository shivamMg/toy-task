$(document).ready(function() {
  var module_columns = "";
  $.each(Modules, function(i, module) {
    console.log(module);
    var column = '<div class="four wide computer six wide tablet column"><button data-handle="'+module.Handle+'"class="ui fluid violet basic large button module-button">' +
      module.Name + '</button><div class="ui fluid inverted popup top left transition hidden">' + module.Description +
      '</div></div>';
    module_columns += column;
  });
  $("#module_buttons").html(module_columns);
  $(".module-button").popup();

  $(document).on("click", ".module-button", function() {
    var module_name = $(this).text();
    var module_handle = $(this).attr("data-handle");
    var key = "module_" + String(Count);
    Pipeline[key] = module_handle;
    var segment = '<div class="ui segment" data-handle="'+module_handle+'" id="'+key+ '">' + module_name +
      '<i class="delete icon ppl-module-cross"></i></div>';
    $("#ppl_modules").append(segment);
    Count += 1;
  });

  $(document).on("click", ".ppl-module-cross", function() {
    var module_id = $(this).parent().attr("id");
    delete Pipeline[module_id];
    $("#" + module_id).remove();
  });

  $("#ppl_upload").click(function(e) {
    e.preventDefault();

    var pipeline = [];
    $.each(Pipeline, function(id, module_handle) {
      pipeline.push(module_handle);
    });

    var form = $("<form>", {
      "action": "/",
      "method": "post"
    }).append($("<input>", {
      "name": "pipeline",
      "value": JSON.stringify(pipeline),
      "type": "hidden"
    }));
    form.submit();
  });
});
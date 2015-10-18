$(document).ready(function(){

	$('.remove-img').addClass('disabled');
		
    $('.add-substancia').on('click', function(e){
		
		$('.midia').clone().insertAfter('.midia:last');
		$('.first:last').prop('class', 'field other-substancies');
		$('.remove-substancia').removeClass('disabled');	

	});

	$('.remove-substancia').on('click', function(){
	
		outrasSubstancias = $('.other-substancies').length;

		if( outrasSubstancias == 1) {
			$('.remove-substancia').addClass('disabled');
		}
		
		$('.other-substancies:last').remove();
	});

});

$( document ).ready( function(){

	window.ajax_setup()
	window.fix_placeholder();

	window.base_wide = 70;
	window.base_divider = 45;
	window.base_subpart = 30;
	window.update_viewport();
	$( window ).resize( window.update_viewport );
	
	//tooltip_init();
	//selection_menu( $( '.editable' ) );

} );

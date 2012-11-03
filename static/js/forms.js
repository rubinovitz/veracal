
function jsonform(elements){
        
                var newContent = {};
                
                
                elements.each(function(){
                
                        // jquery can't do checkboxes
                        // manually build array of checked checkboxes for a given input
                        if( $(this).attr('type') == 'checkbox' ){
                                if( $(this).attr('checked') ){
                                        if( newContent[$(this).attr('name')] )
                                                newContent[$(this).attr('name')].push( $(this).val() );
                                        else 
                                                newContent[$(this).attr('name')] = [ $(this).val() ];
                                }
                        }else if( $(this).attr('type') == 'radio' ){
                                if( $(this).attr('checked') )
                                        newContent[$(this).attr('name')] = $(this).val();
                        // if this isn't a submit/reset/button, add it to our attributes
                        }else if( $.inArray($(this).attr('type'),
                                ['button','submit','reset']) === -1 )
                                // val() resolves selects/textboxes/textareas
                                newContent[$(this).attr('name')] = $(this).val();
                
                });
                
                return JSON.stringify(newContent);

}

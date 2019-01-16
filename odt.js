jQuery('document').ready(function () {
	
    function b64toBlob(b64Data, contentType, sliceSize) {
        contentType = contentType || '';
        sliceSize = sliceSize || 512;
        var byteCharacters = atob(b64Data);
        var byteArrays = [];
        for (var offset = 0; offset < byteCharacters.length; offset += sliceSize) {
            var slice = byteCharacters.slice(offset, offset + sliceSize);
            var byteNumbers = new Array(slice.length);
            for (var i = 0; i < slice.length; i++) {
                byteNumbers[i] = slice.charCodeAt(i);
            }
            var byteArray = new Uint8Array(byteNumbers);
            byteArrays.push(byteArray);
        }
        var blob = new Blob(byteArrays, { type: contentType });
        return blob;
    }
	
    jQuery("#convert-odt").click(function () {
		
        jQuery.loadScript = function (url, callback) {
            jQuery.ajax({
                url: url,
                dataType: 'script',
                success: callback,
                async: true
            });
        }
		
        if (typeof someObject == 'undefined') $.loadScript('https://cdnjs.cloudflare.com/ajax/libs/jszip/2.4.0/jszip.min.js', function () {
			
            var req = new XMLHttpRequest();
            req.open('GET', 'http://www3.gobiernodecanarias.org/medusa/contenidosdigitales/odt/ejemplo.odt');
            req.responseType = 'arraybuffer';
			
            req.addEventListener('load', function () {
				
                var empty = req.response;
                var odtdoc = new ODTDocument(empty);
				
                try {
                    var regex = /<table table:name=\"Tabla1\" class=\"Tabla1\">.*<\/table>/ig;
                    var contenido = $('#contenido').val().replace(/&feature=youtube.be/g, "");
                    contenido = contenido.replace(/&/g, "");
                    contenido = contenido.replace(/<b>/g, "<span class=\"T13\">");
                    contenido = contenido.replace(/<\/b>/g, "<\/span>");
                    contenido = contenido.replace(/<em>/g, "<span class=\"T14\">");
                    contenido = contenido.replace(/<\/em>/g, "<\/span>");
                    contenido = contenido.replace(/<br \/>/g, " ");
                    contenido = contenido.replace(/<ol>/g, "");
                    contenido = contenido.replace(/<\/ol>/g, "");
                    contenido = contenido.replace(/<ul>/g, "");
                    contenido = contenido.replace(/<\/ul>/g, "");
                    contenido = contenido.replace(/<li>/g, "<p>    • ");
                    contenido = contenido.replace(/<\/li>/g, "<\/p>");
                    contenido = contenido.replace(/<p> <\/p>/g, "");
                    //odtdoc.setHTMLUnsafe(odtdoc.getHTMLUnsafe().replace(regex, $('#contenido').val()));
                    odtdoc.setHTMLUnsafe(odtdoc.getHTMLUnsafe().replace(regex, contenido));
                } catch (e) {
                    alert("No se pudo generar el documento odt.");
                    throw e;
                }
				
                var odt = odtdoc.getODT();
                var blob = b64toBlob(odt, "application/vnd.oasis.opendocument.text");
                var link = document.createElement('a');
                link.href = URL.createObjectURL(blob);
                link.download = jQuery('div#nombre-odt').html();
                link.appendChild(
				document.createTextNode('Haga clic aqu\u00ED si su descarga no se inici\u00F3 autom\u00E1ticamente'));
                var downloadArea = document.getElementById('download-area');
                downloadArea.innerHTML = '';
                downloadArea.appendChild(link);
                link.click();
            });
			
            req.send();
            $.loadScript('http://www3.gobiernodecanarias.org/medusa/contenidosdigitales/js/jszip/dist/jszip.min.js');
        });

    });
});

$(document).ready(function(){

    console.log('Ready')

    //  Busque a data atual e atualize-a no DOM
    let dat_time = new Date()
    let current_date = data_time.toLocaleDateString()

    $('#date').text("Data:" + current_date)





    // Escreva um evento, quando o botão Enviar for clicado
    $('#button').click(function(){

        let review = $('#text').val()
        console.log(review)

        let input_data = {'customer_review' : review}
        console.log(input_data)

        //  Obtenha o valor do texto da área de texto usando o método 'val()'
       

        //  Converta-o em um objeto JS.
        //  Forneça uma "chave" aqui e escreva o mesmo no arquivo app.py também para extrair dados


        //  requisição ajax
        $.ajax({

            //  tipo da requisição web
            type : '',

            //  dados a serem enviados no formato JSON
            data : JSON.stringify(),

            //  o tipo de resposta esperado é json
            dataType : 'json',

            //  contentType
            contentType : 'application/json',

            //  se tudo funcionar, execute esta função
            success : function(result){

                // extraia previsão e a URL do emoticon do resultado
                $(document).ready(function(){
                    console.log('Ready')
                
                    let date_time = new Date()
                    let current_date = date_time.toLocaleDateString()
                
                    $('#date').text("Data: " + current_date)
                
                    $('#button').click(function(){
                
                        let review = $('#text').val()
                        console.log(review)
                
                        let input_data = {'customer_review' : review}
                        console.log(input_data)
                
                        $.ajax({
                
                            url : "/predict",
                            type : "POST",
                            data : JSON.stringify(input_data),
                            dataType : 'json',
                            contentType : 'application/json',
                            success : function(result){
                                let prediction = result.prediction
                                let emoji_url = result.url
                                console.log(emoji_url)
                
                                $('#sentiment').text(prediction)
                                $('#sentiment').show()
                
                                $('#emoji').attr('src' , emoji_url)
                                $('#emoji').show()
                            },
                            error : function(result){
                                console.log(result)
                            }
                        })
                
                        $('#text').val("")
                        
                    })
                })


                //  atualize os elementos DOM


                //  exiba-os

            },

            //  se houver algum erro, execute esta função
            error : function(result){

                console.log(result)
            }
        })


        //  limpando a caixa de texto após cada pressionamento de botão
        $('#text').val("")
    })
        
})
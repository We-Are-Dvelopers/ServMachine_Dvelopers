/**
 * WEBSITE: https://themefisher.com
 * TWITTER: https://twitter.com/themefisher
 * FACEBOOK: https://www.facebook.com/themefisher
 * GITHUB: https://github.com/themefisher/
 */

(function ($) {
	'use strict';

	// navbarDropdown
	if ($(window).width() < 992) {
		$('.navigation .dropdown-toggle').on('click', function () {
			$(this).siblings('.dropdown-menu').animate({
				height: 'toggle'
			}, 300);
		});
  }

	// scroll to top button
	$(window).on('scroll', function () {
		if ($(window).scrollTop() > 70) {
			$('.backtop').addClass('reveal');
		} else {
			$('.backtop').removeClass('reveal');
		}
	});
	// scroll-to-top
  $('.scroll-top-to').on('click', function () {
    $('body,html').animate({
      scrollTop: 0
    }, 500);
    return false;
  });

	$('.portfolio-single-slider').slick({
		infinite: true,
		arrows: false,
		autoplay: true,
		autoplaySpeed: 2000
	});

	$('.clients-logo').slick({
		infinite: true,
		arrows: false,
		autoplay: true,
		slidesToShow: 6,
		slidesToScroll: 6,
		autoplaySpeed: 6000,
		responsive: [{
				breakpoint: 1024,
				settings: {
					slidesToShow: 6,
					slidesToScroll: 6,
					infinite: true,
					dots: true
				}
			},
			{
				breakpoint: 900,
				settings: {
					slidesToShow: 4,
					slidesToScroll: 4
				}
			}, {
				breakpoint: 600,
				settings: {
					slidesToShow: 4,
					slidesToScroll: 4
				}
			},
			{
				breakpoint: 480,
				settings: {
					slidesToShow: 2,
					slidesToScroll: 2
				}
			}

		]
	});

	$('.testimonial-wrap').slick({
		slidesToShow: 1,
		slidesToScroll: 1,
		infinite: true,
		dots: true,
		arrows: false,
		autoplay: true,
		vertical: true,
		verticalSwiping: true,
		autoplaySpeed: 6000,
		responsive: [{
				breakpoint: 1024,
				settings: {
					slidesToShow: 1,
					slidesToScroll: 1,
					infinite: true,
					dots: true
				}
			},
			{
				breakpoint: 900,
				settings: {
					slidesToShow: 1,
					slidesToScroll: 1
				}
			}, {
				breakpoint: 600,
				settings: {
					slidesToShow: 1,
					slidesToScroll: 1
				}
			},
			{
				breakpoint: 480,
				settings: {
					slidesToShow: 1,
					slidesToScroll: 1
				}
			}

		]
	});

	$('.testimonial-wrap-2').slick({
		slidesToShow: 2,
		slidesToScroll: 2,
		infinite: true,
		dots: true,
		arrows: false,
		autoplay: true,
		autoplaySpeed: 6000,
		responsive: [{
				breakpoint: 1024,
				settings: {
					slidesToShow: 2,
					slidesToScroll: 2,
					infinite: true,
					dots: true
				}
			},
			{
				breakpoint: 900,
				settings: {
					slidesToShow: 1,
					slidesToScroll: 1
				}
			}, {
				breakpoint: 600,
				settings: {
					slidesToShow: 1,
					slidesToScroll: 1
				}
			},
			{
				breakpoint: 480,
				settings: {
					slidesToShow: 1,
					slidesToScroll: 1
				}
			}

		]
	});


	// counter
	function counter() {
		var oTop;
		if ($('.counter').length !== 0) {
			oTop = $('.counter').offset().top - window.innerHeight;
		}
		if ($(window).scrollTop() > oTop) {
			$('.counter').each(function () {
				var $this = $(this),
					countTo = $this.attr('data-count');
				$({
					countNum: $this.text()
				}).animate({
					countNum: countTo
				}, {
					duration: 500,
					easing: 'swing',
					step: function () {
						$this.text(Math.floor(this.countNum));
					},
					complete: function () {
						$this.text(this.countNum);
					}
				});
			});
		}
  }
  $(window).on('scroll', function () {
		counter();
	});


	// Shuffle js filter and masonry
	if ($('.shuffle-wrapper').length !== 0) {
		var Shuffle = window.Shuffle;
		var jQuery = window.jQuery;

		var myShuffle = new Shuffle(document.querySelector('.shuffle-wrapper'), {
			itemSelector: '.shuffle-item',
			buffer: 1
		});
		jQuery('input[name="shuffle-filter"]').on('change', function (evt) {
			var input = evt.currentTarget;
			if (input.checked) {
				myShuffle.filter(input.value);
			}
		});
	}

})(jQuery);

// async function showInput() {
//     var trainings = document.querySelector('#trainings');
//     var nextPageUrl = 'https://servmachine.com.br/api/professionals';

//     try {
//         while (nextPageUrl) {
//             const response = await fetch(nextPageUrl);
//             if (!response.ok) {
//                 throw new Error(`Erro na requisição: ${response.status}`);
//             }

//             const data = await response.json();

//             // Verifique a estrutura da resposta
//             console.log(data);
//             if (Array.isArray(data.results)) {
//                 data.results.forEach(training => {
//                     if (training.is_old === true) {
//                         var newDiv = document.createElement("div");
//                         newDiv.classList.add("col-4", "d-flex");

//                         let titulo;

//                         if (training.specialty === 'NC') {
//                             titulo = 'Não Cadastrado';
//                         } else if (training.specialty === 'OP') {
//                             titulo = 'Operador de Máquina Perfuratriz';
//                         } else if (training.specialty === 'NA') {
//                             titulo = 'Navegador de Perfuração Direcional';
//                         } else if (training.specialty === 'MP') {
//                             titulo = 'Mapeador de Interferência';
//                         } else if (training.specialty === 'IN') {
//                             titulo = 'Inspetor de Perfuração Direcional';
//                         } else if (training.specialty === 'OU') {
//                             titulo = 'Outro';
//                         }

//                         newDiv.innerHTML = `
//                             <img src="https://servmachine.com.br/media/default_profile.jpg" alt="Profile Image" style="height: 200px;">
//                             <div class="conteudo">
//                                 <h5>${titulo}</h5>
//                                 <h3>${training.name}</h3>
//                                 <p>Para maiores informações, entre em contato conosco</p>
//                                 <a href="mailto:contato@servmachine.com.br" class="btn btn-sm btn-success text-center" target="_blank">Entrar em contato</a>
//                             </div>
//                         `;

//                         trainings.appendChild(newDiv);
//                     }
//                 });
//             } else {
//                 console.error("A estrutura da resposta não é a esperada.");
//             }

//             nextPageUrl = data.next; // Atualize a URL da próxima página
//         }
//     } catch (error) {
//         console.error("Erro ao buscar os dados:", error);
//     }
// }


async function showInpu2() {
    var trainings = document.querySelector('#trainings');

    const response = await fetch('https://servmachine.com.br/api/professionals');
    const data = await response.json();

    data.forEach(training => {
        if (training.is_old == true){
			var newDiv = document.createElement("div");
			newDiv.classList.add("col-md-10", "col-12", "mt-5");
			var cardDiv = document.createElement("div");
			cardDiv.classList.add("card");

			cardDiv.innerHTML = `
			<div class="col-4 d-flex">
				<img src="${training.picture}" alt="" style="height: 200px;">
				<div class="conteudo">
					<h5>${training.specialty}</h5>
					<h3>${training.surname}</h3>
					<p>Para maiores informações, entre em contato conosco</p>
					<a href="" class="btn btn-sm btn-success text-center" target="_blank">Entrar em contato</a>
				</div>
			</div>
			`;

				newDiv.appendChild(cardDiv);

				trainings.appendChild(newDiv);
				console.log(training);
		}
    });
}
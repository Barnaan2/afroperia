/**
 * Template Name: Logis - v1.0.1
 * Template URL: https://bootstrapmade.com/logis-bootstrap-logistics-website-template/
 * Author: BootstrapMade.com
 * License: https://bootstrapmade.com/license/
 */
document.addEventListener('DOMContentLoaded', () => {
    "use strict";

    /**
     * Preloader
     */
    const preloader = document.querySelector('#preloader');
    if (preloader) {
        window.addEventListener('load', () => {
            preloader.remove();
        });
    }

    /**
     * Sticky header on scroll
     */
    const selectHeader = document.querySelector('#header');


    /**
     * Scroll top button
     */
    const scrollTop = document.querySelector('.scroll-top');
    if (scrollTop) {
        const togglescrollTop = function() {
            window.scrollY > 100 ? scrollTop.classList.add('active') : scrollTop.classList.remove('active');
        }
        window.addEventListener('load', togglescrollTop);
        document.addEventListener('scroll', togglescrollTop);
        scrollTop.addEventListener('click', window.scrollTo({
            top: 0,
            behavior: 'smooth'
        }));
    }

    /**
     * Mobile nav toggle
     */
    const mobileNavShow = document.querySelector('.mobile-nav-show');
    const mobileNavHide = document.querySelector('.mobile-nav-hide');

    document.querySelectorAll('.mobile-nav-toggle').forEach(el => {
        el.addEventListener('click', function(event) {
            event.preventDefault();
            mobileNavToogle();
        })
    });

    function mobileNavToogle() {
        document.querySelector('body').classList.toggle('mobile-nav-active');
        mobileNavShow.classList.toggle('d-none');
        mobileNavHide.classList.toggle('d-none');
    }

    /**
     * Hide mobile nav on same-page/hash links
     */
    document.querySelectorAll('#navbar a').forEach(navbarlink => {

        if (!navbarlink.hash) return;

        let section = document.querySelector(navbarlink.hash);
        if (!section) return;

        navbarlink.addEventListener('click', () => {
            if (document.querySelector('.mobile-nav-active')) {
                mobileNavToogle();
            }
        });

    });

    /**
     * Toggle mobile nav dropdowns
     */
    const navDropdowns = document.querySelectorAll('.navbar .dropdown > a');

    navDropdowns.forEach(el => {
        el.addEventListener('click', function(event) {
            if (document.querySelector('.mobile-nav-active')) {
                event.preventDefault();
                this.classList.toggle('active');
                this.nextElementSibling.classList.toggle('dropdown-active');

                let dropDownIndicator = this.querySelector('.dropdown-indicator');
                dropDownIndicator.classList.toggle('bi-chevron-up');
                dropDownIndicator.classList.toggle('bi-chevron-down');
            }
        })
    });

    /**
     * Initiate pURE cOUNTER
     */
    new PureCounter();

    /**
     * Initiate glightbox
     */
    const glightbox = GLightbox({
        selector: '.glightbox'
    });

    /**
     * Init swiper slider with 1 slide at once in desktop view
     */
    new Swiper('.slides-1', {
        speed: 600,
        loop: true,
        autoplay: {
            delay: 5000,
            disableOnInteraction: false
        },
        slidesPerView: 'auto',
        pagination: {
            el: '.swiper-pagination',
            type: 'bullets',
            clickable: true
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        }
    });

    /**
     * Animation on scroll function and init
     */
    function aos_init() {
        AOS.init({
            duration: 1000,
            easing: 'ease-in-out',
            once: true,
            mirror: false
        });
    }
    window.addEventListener('load', () => {
        aos_init();
    });

});

//checkin checkout

function convertToISO(timebit) {
    timebit.setHours(0, -timebit.getTimezoneOffset(), 0, 0);
    // remove GMT offset
    var isodate = timebit.toISOString().slice(0, 10);
    // format convert and take first 10 characters of result
    return isodate;
}
var checkin = document.getElementById('checkin'),
    currentdate = new Date();
checkin.min = convertToISO(currentdate);
checkin.placeholder = checkin.min;
var futuredate = new Date();
futuredate.setDate(futuredate.getDate() + 7);
// go forward 7 days into the future
checkin.max = convertToISO(futuredate);

var checkout = document.getElementByID('checkout'),
    currentdate = new Date();
checkout.min = convertToISO(currentdate);
checkout.placeholder = checkout.min;
var checkoutfuture = new Date();
checkoutfuture.setDate(checkoutfuture.getDate() + 14);

checkout.max = convertToISO(checkoutfuture);


$(document).ready(function() {
    $('.count').prop('disabled', false);
    $(document).on('click', '.plus', function() {
        $('.count').value(parseInt($('.count').value()) + 1);
    });
    $(document).on('click', '.minus', function() {
        $('.count').value(parseInt($('.count').value()) - 1);
        if ($('.count').value() == 0) {
            $('.count').value(1);
        }
    });
});
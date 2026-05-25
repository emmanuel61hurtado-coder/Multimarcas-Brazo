var shareQRGenerated = false;

function getShareURL() {
    return window.location.href;
}

function getShareText() {
    return 'Mirá esto de Multimarcas Brazo: ' + document.title;
}

function toggleSharePanel() {
    var panel = document.getElementById('sharePanel');
    var trigger = document.getElementById('shareTrigger');
    panel.classList.toggle('show');
    trigger.classList.toggle('active');
}

function shareFacebook() {
    var url = 'https://www.facebook.com/sharer/sharer.php?u=' + encodeURIComponent(getShareURL());
    window.open(url, '_blank', 'width=600,height=400');
    closeSharePanel();
}

function shareWhatsApp() {
    var url = 'https://wa.me/?text=' + encodeURIComponent(getShareText() + ' ' + getShareURL());
    window.open(url, '_blank');
    closeSharePanel();
}

function shareInstagram() {
    if (navigator.share) {
        navigator.share({
            title: document.title,
            text: getShareText(),
            url: getShareURL()
        }).catch(function() {});
    } else {
        copyLink();
        var btn = document.querySelector('.share-option[onclick="shareInstagram()"] span');
        if (btn) btn.textContent = 'Link copiado';
        setTimeout(function() {
            if (btn) btn.textContent = 'Instagram';
        }, 2000);
    }
    closeSharePanel();
}

function copyLink() {
    var url = getShareURL();
    if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(url).then(function() {
            showCopyToast();
        }).catch(function() {
            fallbackCopy(url);
        });
    } else {
        fallbackCopy(url);
    }
    closeSharePanel();
}

function fallbackCopy(text) {
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand('copy'); showCopyToast(); } catch(e) {}
    document.body.removeChild(ta);
}

function showCopyToast() {
    var toast = document.getElementById('toastCopy');
    if (!toast) return;
    toast.classList.remove('d-none');
    toast.classList.add('show');
    setTimeout(function() {
        toast.classList.add('d-none');
        toast.classList.remove('show');
    }, 2500);
}

function toggleQR() {
    var section = document.getElementById('qrSection');
    section.classList.toggle('d-none');
    if (!section.classList.contains('d-none') && !shareQRGenerated) {
        shareQRGenerated = true;
        if (typeof QRCode !== 'undefined') {
            new QRCode(document.getElementById('qrcode'), {
                text: getShareURL(),
                width: 160,
                height: 160,
                colorDark: '#ffffff',
                colorLight: '#0a0a0c',
                correctLevel: QRCode.CorrectLevel.H
            });
        }
    }
}

function closeSharePanel() {
    var panel = document.getElementById('sharePanel');
    var trigger = document.getElementById('shareTrigger');
    panel.classList.remove('show');
    trigger.classList.remove('active');
}

document.addEventListener('click', function(e) {
    var float = document.getElementById('shareFloat');
    if (float && !float.contains(e.target)) {
        var panel = document.getElementById('sharePanel');
        var trigger = document.getElementById('shareTrigger');
        if (panel && panel.classList.contains('show')) {
            panel.classList.remove('show');
            trigger.classList.remove('active');
        }
    }
});
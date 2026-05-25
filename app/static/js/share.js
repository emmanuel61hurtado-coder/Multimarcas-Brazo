var shareQRGenerated = false;

function getShareURL() {
    return window.location.href;
}

function getShareText() {
    return 'Mirá esto de Multimarcas Brazo: ' + document.title;
}

function closeShareModal() {
    var modal = bootstrap.Modal.getInstance(document.getElementById('shareModal'));
    if (modal) modal.hide();
}

function shareFacebook() {
    var url = 'https://www.facebook.com/sharer/sharer.php?u=' + encodeURIComponent(getShareURL());
    window.open(url, '_blank', 'width=600,height=400');
    closeShareModal();
}

function shareWhatsApp() {
    var url = 'https://wa.me/?text=' + encodeURIComponent(getShareText() + ' ' + getShareURL());
    window.open(url, '_blank');
    closeShareModal();
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
    }
    closeShareModal();
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
    closeShareModal();
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

// Reset QR on modal close
document.addEventListener('DOMContentLoaded', function() {
    var modal = document.getElementById('shareModal');
    if (modal) {
        modal.addEventListener('hidden.bs.modal', function() {
            var section = document.getElementById('qrSection');
            if (section) section.classList.add('d-none');
            var qr = document.getElementById('qrcode');
            if (qr) qr.innerHTML = '';
            shareQRGenerated = false;
        });
    }
});
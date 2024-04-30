function setQRCodeGeneratedCookie() {
    document.cookie = "qrcodeGenerated=true; expires=; path=/";
}

function generateQRCode(weeks) {
    const qrCodeContainer = document.getElementById('qr-code');
    const ticketDetails = document.getElementById('ticket-details');
    const location = document.getElementById('location').value;
    const qrCodeContainerDiv = document.getElementById('qr-code-container');
    const downloadButton = document.getElementById('download-button');

    qrCodeContainerDiv.style.display = 'flex'; 

    const months = Math.floor(weeks / 4);
    const remainingWeeks = weeks % 4;

    const ticketPrices = {
        Nelspruit: 120,
        Lekazi: 144,
        Kabokweni: 127,
        Kabokweni: 127,
        Matsulu_Depot: 113,
        Emoyeni_Mall:109,
        Boxer_Nelspruit:99,
        Boxer_Promenade:111,
        Boxer_Kanyamazane:115,
        Boxer_Matsulu:240,
        Boxer_Naas:140,
        Boxer_Schoemansdal:200,
        Boxer_Hazyview:154,
        Movo_Kabokweni:134,
        Coast_to_Coast_Jeppes_Reef:120,
        JE_Travel_Hazyview_Spar:113,
        Malalane_Spar:220,
        white_River_Spar:100,
        MSM_Distributors_Lekazi:122,
        Bongani_Kwa_Msibi:132,

    };

    const totalPrice = ticketPrices[location] * weeks;

    const qrcode = new QRCode(qrCodeContainer, {
        text: `Destination: ${location}\nNumber of Weeks: ${weeks}\nTotal Cost: R${totalPrice}`,
        width: 200,
        height: 200,
    });

    if (months > 0 && remainingWeeks === 0) {
        ticketDetails.textContent = `You bought tickets for ${months} month(s).`;
    } else {
        ticketDetails.textContent = `You bought tickets for ${weeks} week(s) to ${location}. Total Cost: R${totalPrice}.`;
    }

    ticketDetails.style.display = 'block';

    downloadButton.style.display = 'block';
    downloadButton.addEventListener('click', () => {
        const canvas = qrCodeContainer.querySelector('canvas');
        const qrCodeImage = canvas.toDataURL('image/png');

        const a = document.createElement('a');
        a.href = qrCodeImage;
        a.download = 'qrcode.png';
        a.click();
    });
}

const purchaseButton = document.getElementById('purchase-button');
purchaseButton.addEventListener('click', () => {
    const weeks = parseInt(document.getElementById('weeks').value);
    generateQRCode(weeks);
});
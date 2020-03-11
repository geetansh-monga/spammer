import smtplib
from email.message import EmailMessage 


print('Setup...')
count = 0
server = smtplib.SMTP('smtp.gmail.com', 587 )
server.ehlo()
server.starttls()
server.ehlo()
server.login('xyz@gmail.com', '')

data = 

for email in data: 
    msg = EmailMessage()
    msg['Subject'] = 'Confirmation/RSVP for the MLH localhost'
    msg['From'] = 'localhost@vipsace.org' 
    msg['To'] = f"{email}"
    msg.set_content(
        """<!DOCTYPE html> <html style="padding: 0;margin: 0;height: 100%;"> <head style="padding: 0;margin: 0;">
            <title style="padding: 0;margin: 0;">MLH localhost - Powered by ACE | Invitation</title>
            <meta charset="utf-8" style="padding: 0;margin: 0;">
            <meta name="viewport" content="width=device-width,initial-scale=1.0" style="padding: 0;margin: 0;">
            <style type="text/css" style="padding: 0;margin: 0;">
        *{
            
            padding:0;
            margin: 0;
        }
        
        body {
            
            color: black;
            margin: 0px;
            background: black;
            padding: 0px;
            width: 100%;
            height: 100%;
            overflow-x: hidden;
        }
        
        html, body {
            
            height: 100%;
        }
        
        *:focus {
            
            outline: none;
        }
        
        a, a:hover, a:focus, a:clicked {
            
            color: #fff;
        }
        
        .main {
            
            width: 100%;
        }
        
        .wrap-main {
            
            position: relative;
            margin: 0 auto;
            width: 500px;
            background: white;
            padding-bottom: 20px;
            text-align: center;
            max-width: 100%;
        }
        
        .blue-back {
            max-width: 100%;
            width: 500px;
            background: #04306d;
            height: 300px;
        }
        
        .blue-back img {
            
            width: 90px;
            margin:0 auto;
            margin-top: 15px;
        }
        
        .white-block {
            
            width: 350px;
            background: white;
            text-align: center;
            padding: 30px;
            box-shadow: 0px 1px 7px #80808033;
            border-radius: 20px;
            position: absolute;
            top: 90px;
            z-index: 2;
            overflow: hidden;
            margin: 0 auto;
            left:0;
            right:0;
        }
        
        .white-block h1 {
            
            text-align: left;
            font-family: 'Open Sans Condensed';
            font-weight: 700;
            color: #04306d;
            line-height: 110%;
            font-size: 30px;
            margin-top: 10px;
        }
        
        .white-block h1 span {
            
            color: #26b6ed;
        }
        
        .white-block .line {
            
            width: 100px;
            margin-top: 5px;
            margin-left: 2px;
            height: 4px;
            background: #26b6ed;
        }
        
        .wrap-main .content-wrap {
            
            margin: 0 auto;
            width: 355px;
            text-align: center;
            margin-top:0px;
        }
        
        .wrap-main .content-wrap p {
            
            font-family: 'Open Sans';
            font-size: 13px;
            line-height: 150%;
            color: #6f6f6f;;
            text-align: justify;
        }
        
        .wrap-main .content-wrap button {
            
            background: #04306d;
            border-radius: 10px;
            cursor: pointer;
            border:none;
            color: white;
            font-size: 20px;
            padding: 10px;
            width: 300px;
            margin: 0 auto;
            font-weight: 600;
            border-bottom: 6px solid #26b6ed;
            transition: border-bottom 0.2s linear;
            font-family: 'Open Sans Condensed';
        }
        
        .wrap-main .content-wrap button:active {
            
            border-bottom: 0px solid #26b6ed;
            transition: border-bottom 0.2s linear;
        }
        
        .wrap-main .content-wrap .wrap {
            
            display: inline-block;
            width: 49%;
        }
        
        .wrap-main .content-wrap .wrap p {
            
            font-family: 'Open Sans';
            color: #6f6f6f;
            font-size: 13px;
        }
        
        .wrap-main .content-wrap h2 i {
            
            color: #26b6ed;
        }
        
        .wrap-main .content-wrap h2 {
            
            color: #04306d;
            font-size: 13px;
            margin-top: 20px;
            letter-spacing: 1px;
            font-weight: 700;
            text-transform: uppercase;
            font-family: 'Open Sans Condensed';
        }
        
        .wrap-main .content-wrap h2 img {
            
            width: 15px;
            vertical-align: middle;
        }
        
        .wrap-main .content-wrap .wrap p a.email {
            
            font-weight: bold !important;
            color: black !important;
        }
        
        .wrap-main .content-wrap .wrap img {
            
            width: 15px;
            color: #04306d;
            margin: 3px;
            vertical-align: middle;
        }
        
        .white-block img {
            
            width: 140px;
        }
        
        .wrap-main .content-wrap .wrap right {
            
            text-align: right;
        }
        
        .wrap-main .content-wrap .wrap left {
            
            text-align: left;
        }
        
        .upper {
            max-width: 100vw;;
            width: 100%;
        }
        
        @media screen and (max-width:900px) {
            
            .wrap-main {
                width: 90%!important;
            }
            .blue-back {
                width: 100%!important;
            }
            .wrap-main .white-block {
                width: 70%!important;
            }
            .wrap-main .white-block img {
                width: 100px!important;
            }
            .wrap-main  .white-block h1 {
                font-size: 25px!important;
            }
            .wrap-main .content-wrap {
                width: 70%!important;
            }
            .wrap-main .content-wrap button {
                width: 100%!important;
                font-size: 18px!important;
                padding: 10px!important;
            }
            .wrap-main .content-wrap .wrap {
                text-align: center !important;
                width: 100% !important;
                margin-top: 5px !important;
            }
            .wrap-main .content-wrap .wrap p {
                text-align: center !important;
            }
            body {
                background:#fff!important;
            }
        }
        
    </style>
</head> <body style="padding: 0px;margin: 0px;color: black;background: black;width: 100%;height: 100%;overflow-x: hidden;">
    
    <div class="main" style="padding: 0;margin: 0;width: 100%;">
        <div class="wrap-main" style="padding: 0;margin: 0 auto;position: relative;width: 500px;background: white;padding-bottom: 20px;text-align: center;max-width: 100%;">
            <a href="https://hack-vsit.tech?ref=mail" target="_blank" style="padding: 0;margin: 0;color: #fff;"><img src="https://lh3.googleusercontent.com/DZeA8epuTfOrlc8nUDlBpQbXtjQw-bSEsqXscaVnWrqcvw-b0XXiTh_i2Dtz3s1CXKLLdblp1KuuMJ6haaquyKhAWR7rp8AvsWoCh4s7CNk0us6V2yILoBhyLr-8-755uT1VSjQR9bJn0RW3695MFj5VQskyrzJMzFdPq_MfxvHbNR3c8_nQZRQkuXybqoxG5C3bvgRSyfNG2nzeBVpkag6-Ejo4mirXEgDVm94E_bRkQRTpPbSWQtw7CPzEoXfy_GHtaSvsiGqwE2fcB1_NaeTaWTEeEpmfeTuMLk-zHE1ud8b7g1hakajyYRCn91qRDNzbFQWbvBMrCdJ_c7df2zyvEp12cNyQpohLMF543b7PoLqOE6sALKYH9GoNE5m1cGM9lU-Ndtzm4gAY7vyTMsS0J5iqjoV7ztIMcap8_4dVBsuAtoR0gfNPSdQsY-SgVHtzppcWz9DoHXXejjF2dRSL2PCrLYj2CFlrydp8L4cyqX3U1VHYSSjIYXaXs2FOkwRx0294jwj2k6UTramckkDbkb40SGM-EAqh0AW3oEw7EAM9pxSToIaXGcDwfOJr3nVsUNidYzE8XV5CDK6icZcy0s9cTQ0MtqjeHrfEdRK8eg7--tnpbT-Ipke2_R4bNQejXUXlsT5CPJHFSlmMSKMr1HjmzuQTOhHK-jAQMxuJVRVcPqN2hSiuPqp_5ZF0fn5snzNkF1kzm_Phfm0P8aUDFYda_vf_zOZDwlQUrTCVWpvE=s608-no" class="upper" style="padding: 0;margin: 0;max-width: 100vw;width: 100%;"></a>
            <div class="content-wrap" style="padding: 0;margin: 0 auto;width: 355px;text-align: center;margin-top: 0px;">
                <p style="font-family: sans-serif;padding: 0;margin: 0;font-size: 13px;line-height: 150%;color: #6f6f6f;text-align: justify;">
                    <br style="padding: 0;margin: 0;"><br style="padding: 0;margin: 0;">
                    <strong style="padding: 0;margin: 0;">ACE - The Technical society of VIPS</strong> is organising an <strong style="padding: 0;margin: 0;">MLH localhost workshop </strong> to enhance skills with cloud 
                    computing and how to deploy the app to a secure DigitalOcean Droplet and learn core principles of 
                    <strong style="padding: 0;margin: 0;">Developer Operations (DevOps) </strong>
                    such as Security, High Availability, and Monitoring to streamline 
                    production applications.
                    <br style="padding: 0;margin: 0;"><br style="padding: 0;margin: 0;">
                    Confirm your presence along with your laptop to make your way into this realm.
                    <br style="padding: 0;margin: 0;"><br style="padding: 0;margin: 0;">
                    <strong style="padding: 0;margin: 0;">Topic:</strong> App deployment and Security with Digital Ocean.
                    <br style="padding: 0;margin: 0;"><br style="padding: 0;margin: 0;">
                    <strong style="padding: 0;margin: 0;">Date:</strong> 20/01/20
                    <br style="padding: 0;margin: 0;"><br style="padding: 0;margin: 0;">
                    <strong style="padding: 0;margin: 0;">Timings:</strong> 11:00 AM to 1:00 PM.
                    <br style="padding: 0;margin: 0;"><br style="padding: 0;margin: 0;">
                    <strong style="padding: 0;margin: 0;">Why should you join?:</strong> it's completely free and will provide you with certificates to enhance your CV.
                    <br style="padding: 0;margin: 0;"><br style="padding: 0;margin: 0;">
                    <strong style="padding: 0;margin: 0;">When:</strong> 20th January 2020<br style="padding: 0;margin: 0;">
                    <br style="padding: 0;margin: 0;">
                    <strong style="padding: 0;margin: 0;">Venue: </strong><a href="https://goo.gl/maps/Fse22yYRvZzEL9MW7" target="_blank" rel="noopener noreferrer" style="text-decoration: none;color: inherit;padding: 0;margin: 0;text-align: left;">Vivekananda Institute of Professional Studies, Pitampura</a>
                    <br style="padding: 0;margin: 0;"><br style="padding: 0;margin: 0;">
                    <a href="https://vipsace.typeform.com/to/Yq8eKR" style="padding: 0;margin: 0;color: #fff;"><button style="font-family: sans-serif;font-stretch: ultra-condensed;padding: 10px;margin: 0 auto;background: purple;border-radius: 10px;cursor: pointer;border: none;color: white;font-size: 20px;width: 300px;font-weight: 600;border-bottom: 6px solid rgb(77, 1, 77);transition: border-bottom 0.2s linear;">RSVP</button></a>
                    <br style="padding: 0;margin: 0;"><br style="padding: 0;margin: 0;"><br style="padding: 0;margin: 0;">
                    <div class="wrap left" style="padding: 0;margin: 0;display: inline-block;width: 49%;">
                        <p style="font-family: sans-serif;padding: 0;margin: 0;font-size: 13px;line-height: 150%;color: #6f6f6f;text-align: justify;">For more info <a href="mailto:csi-sb-ace@vips.edu'," class="email" style="padding: 0;margin: 0;color: black !important;font-weight: bold !important;">email us</a></p>
                    </div>
                    <div class="wrap right" style="padding: 0;margin: 0;display: inline-block;width: 49%;">
                        <a href="8447838327" style="padding: 0;margin: 0;color: #fff;">
                        <a href="mailto:csi-sb-ace@vips.edu'," target="_blank" style="padding: 0;margin: 0;color: #fff;"><img src="https://png.icons8.com/color/540/gmail.png" style="padding: 0;margin: 3px;width: 15px;color: #04306d;vertical-align: middle;"></a>
                        <a href="https://www.facebook.com/vipsace/" target="_blank" style="padding: 0;margin: 0;color: #fff;"><img src="https://cdnjs.cloudflare.com/ajax/libs/webicons/2.0.0/webicons/webicon-facebook-s.png" style="padding: 0;margin: 3px;width: 15px;color: #04306d;vertical-align: middle;"></a>
                        <a href="http://twitter.com/vips_ace" target="_blank" style="padding: 0;margin: 0;color: #fff;"><img src="https://cdnjs.cloudflare.com/ajax/libs/webicons/2.0.0/webicons/webicon-twitter-s.png" style="padding: 0;margin: 3px;width: 15px;color: #04306d;vertical-align: middle;"></a>
                        <a href="https://www.instagram.com/acevips/" target="_blank" style="padding: 0;margin: 0;color: #fff;"><img src="https://cdnjs.cloudflare.com/ajax/libs/webicons/2.0.0/webicons/webicon-instagram-s.png" style="padding: 0;margin: 3px;width: 15px;color: #04306d;vertical-align: middle;"></a>
                        <a href="https://hack-vsit.tech/" target="_blank" style="padding: 0;margin: 0;color: #fff;"><img src="http://wfarm3.dataknet.com/static/resources/icons/set114/4705939d.png" style="padding: 0;margin: 3px;width: 15px;color: #04306d;vertical-align: middle;"></a>
                        <a href="https://github.com/vipsace/" target="_blank" style="padding: 0;margin: 0;color: #fff;"><img src="https://cdnjs.cloudflare.com/ajax/libs/webicons/2.0.0/webicons/webicon-github-s.png" style="padding: 0;margin: 3px;width: 15px;color: #04306d;vertical-align: middle;"></a>
                    </div>
                    <h2 style="font-family: sans-serif;font-stretch: ultra-condensed;padding: 0;margin: 0;color: #04306d;font-size: 13px;margin-top: 20px;letter-spacing: 1px;font-weight: 700;text-transform: uppercase;">MADE WITH <img src="https://cdn3.iconfinder.com/data/icons/cosmo-color-basic-1/40/favorite-512.png" style="padding: 0;margin: 0;width: 15px;vertical-align: middle;"> <a href="https://vipsace.org/" style="text-decoration: none;color: inherit;padding: 0;margin: 0;">BY ACE</a></h2>
                </div>
            </div>
        </div>
        <img src="{{ TRACKING_URL }}" style="visibility: hidden;"/>
    </body> </html>""", subtype = 'html')

    server.send_message(msg)
    print('sent')
    count = count + 1

print(count)

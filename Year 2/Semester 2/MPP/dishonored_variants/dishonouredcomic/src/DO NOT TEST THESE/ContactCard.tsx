import "./ContactCard.css";
import heroImg from "../assets/hero.png";

const ContactCard = () => {
  return (
    <>
      <div className="main-div-contact">
        <h3 className="title-contact">Contact</h3>
        <div className="socials-container">
          <a href="" className="socials-card">
            <div>
              <img src={heroImg} alt="" className="socials-icon"></img>
              <div className="socials-title">Email</div>
            </div>
          </a>

          <a href="" className="socials-card">
            <div>
              <img src={heroImg} alt="" className="socials-icon"></img>
              <div className="socials-title">Instagram</div>
            </div>
          </a>
          <a href="" className="socials-card">
            <div>
              <img src={heroImg} alt="" className="socials-icon"></img>
              <div className="socials-title">Patreon</div>
            </div>
          </a>
        </div>
      </div>
    </>
  );
};

export default ContactCard;

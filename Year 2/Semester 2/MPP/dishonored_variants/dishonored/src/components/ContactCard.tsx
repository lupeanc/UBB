import "./ContactCard.css";
import heroImg from "../assets/hero.png";
import { motion } from "motion/react";

const ContactCard = () => {
  return (
    <>
      <div className="main-div-contact">
        <h3 className="title-contact">Contact</h3>
        <div className="socials-container">
          <a href="" className="socials-card">
            <motion.div whileHover={{ scale: 1.1 }} whileTap={{ scale: 1 }}>
              <img src={heroImg} alt="" className="socials-icon"></img>
              <div className="socials-title">Email</div>
            </motion.div>
          </a>

          <a href="" className="socials-card">
            <motion.div whileHover={{ scale: 1.1 }} whileTap={{ scale: 1 }}>
              <img src={heroImg} alt="" className="socials-icon"></img>
              <div className="socials-title">Instagram</div>
            </motion.div>
          </a>
          <a href="" className="socials-card">
            <motion.div whileHover={{ scale: 1.1 }} whileTap={{ scale: 1 }}>
              <img src={heroImg} alt="" className="socials-icon"></img>
              <div className="socials-title">Patreon</div>
            </motion.div>
          </a>
        </div>
      </div>
    </>
  );
};

export default ContactCard;

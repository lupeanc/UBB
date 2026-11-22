import ContactCard from "../components/ContactCard";
import QnACard from "../components/QnACard";
import WantMoreBanner from "../components/WantMoreBanner";
import "./AboutPage.css";

export type QnAType = {
  question: string;
  answer: string;
};

const AboutPage = () => {
  const qnas: Array<QnAType> = [
    {
      question: "When will the next chapter be posted?",
      answer: "Wouldn't you like to know, weather boy? (Next week)",
    },
    {
      question: "How long does it take you to design a character?",
      answer: "Depends on the character really. Couple of days - a week.",
    },
    {
      question: "Where can I find more of your content?",
      answer:
        "Any/all social platforms :) @dishonouredcomic. ~Extra content posted on Patreon! (link below)",
    },
    {
      question: "Is fanart okay to do?",
      answer:
        "WE WOULD BE HONOURED NGL!! Tag us if you post it/send it to us if you dont :)",
    },
    {
      question: "Nu mai am idei de intrebari",
      answer: "Nici io de raspunsuri. bate palma",
    },
    {
      question: "test question sa vedem ce face cu text lung",
      answer:
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    },
  ];

  return (
    <>
      <div className="main-div-about">
        <div className="about-container">
          <h2 className="title-about">Frequently Asked Questions</h2>
          <br></br>
          {qnas.map((qna) => (
            <QnACard qna={qna} />
          ))}
          <WantMoreBanner />
          <hr color="#3a3a3d"></hr>
          <ContactCard />
        </div>
      </div>
    </>
  );
};

export default AboutPage;

import "./QnACard.css";

const QnACard = ({ qna }) => {
  return (
    <>
      <div className="qna-div">
        <div className="question">Q: {qna.question}</div>
        {/* <hr color="rgb(42, 42, 42)"></hr> */}
        <div className="answer">
          <b>A: </b> {qna.answer}
        </div>
        <hr color="#3a3a3d"></hr>
      </div>
    </>
  );
};

export default QnACard;

<?php

use Couchbase\User;
use repo\DBUtils;

require_once '../repo/DBUtils.php';
class Database
{
    private $db;

    public function __construct(){
        $this->db = new DBUtils();
    }

    public function getUserArticles($username){
        $res = $this->db->getUserArticles($username);
        $articles = array();
        foreach($res as $key => $value){
            $article = new Article($value['id'], $value['user'], $value['journalid'], $value['summary'], $value['date']);
            array_push($articles, $article);
        }

        return $articles;
    }

    public function getUserArticlesByJournals($username, $name){
        $res = $this->db->getUserArticlesByJournals($username, $name);
        $articles = array();
        foreach($res as $key => $value){
            $article = new Article($value['id'], $value['user'], $value['journalid'], $value['summary'], $value['date']);
            array_push($articles, $article);
        }
        return $articles;
    }

    public function getJournalNamesForUser($username){
        $res = $this->db->getJournalNamesForUser($username);
        $names = array();
        foreach($res as $key => $value){
            array_push($names, $value['name']);
        }
        return $names;
    }

    public function getUser($username){
        $res = $this->db->getUser($username);
        return $res;
    }

    public function addArticle($username, $journalid, $summary, $date, $journalname)
    {
        $res = $this->db->addArticle($username, $journalid, $summary, $date, $journalname);
        return $res;
    }

    public function deleteArticle($id){
        $res = $this->db->deleteArticle($id);
        return $res;
    }

    public function updateArticle($id, $user, $journalid, $summary, $date, $journalname){
        $res = $this->db->updateArticle($id, $user, $journalid, $summary, $date, $journalname);
        return $res;
    }
}
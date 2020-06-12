<h1>Create new book</h1>
<?php
    $options = array('drama' =>'drama', 'comedy' =>'comedy');
    echo $this->Form->create('Book');
    echo $this->Form->input('title');
    echo $this->Form->input('author');
    echo $this->Form->input('genre',
    array('options'=>$options, 'default'=>'drama'));
    echo $this->Form->end('Save');
?>
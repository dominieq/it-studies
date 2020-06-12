<h1>Edit book</h1>

<?php
    $options = array('drama' => 'drama','comedy' => 'comedy');
    echo $this->Form->create('Book', array('url' => 'edit'));
    echo $this->Form->input('id', array('type' => 'hidden'));
    echo $this->Form->input('title');
    echo $this->Form->input('author');
    echo $this->Form->input('genre',
    array('options'=>$options, 'default'=>'drama'));
    echo $this->Form->end('Save');
?>
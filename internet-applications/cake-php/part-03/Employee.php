<?php
App::uses('AppModel', 'Model');
/**
 * Employee Model
 *
 */
class Employee extends AppModel {

    var $validate = array(

        'nazwisko' => array(
            'rule' => 'notBlank',
            'required' => true,
            'message' => 'Input required'
        ),

        'etat' => array(
            'rule' => 'notBlank',
            'required' => true,
            'message' => 'Input required'
        ),

        'placa_pod' => array(

            'placa_pod_rule_1' => array(
                'rule' => 'numeric',
                'message' => 'Input must be a number'
            ),

            'placa_pod_rule_2' => array(
                'rule' => array('range', -0.01, 2000.01),
                'message' => 'Number must be between 0 and 2000'
            )
        )
    );
}

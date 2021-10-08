# Learning setting
from cords.utils.data.datasets.SSL.augmentation.augmentation_pool import ZCA


config = dict(setting="SSL",

              dataset=dict(name="cifar10",
                           datadir="../data",
                           feature="dss",
                           type="pre-defined",
                           whiten=False,
                           zca=True,
                           labeled_aug='WA',
                           unlabeled_aug='WA',
                           wa = 't.t.f',
                           strong_aug=False),

              dataloader=dict(shuffle=True,
                              pin_memory=True,
                              num_workers=8,
                              l_batch_size=50,
                              ul_batch_size=50),

              model=dict(architecture='wrn',
                         type='pre-defined',
                         numclasses=10),
              
              ckpt=dict(is_load=False,
                        is_save=True,
                        dir='results/',
                        save_every=20),
              
              loss=dict(type='CrossEntropyLoss',
                        use_sigmoid=False),

              optimizer=dict(type="sgd",
                             momentum=0.9,
                             lr=0.03,
                             weight_decay=5e-4),

              scheduler=dict(type="cosine_annealing",
                             T_max=300),

              dss_args=dict(type="GLISTER",
                                fraction=0.1,
                                select_every=20,
                                kappa=0,
                                linear_layer=False,
                                selection_type='Supervised',
                                greedy='Stochastic'),

              train_args=dict(num_epochs=300,
                              device="cuda",
                              print_every=10,
                              results_dir='results/',
                              print_args=["val_loss", "val_acc", "tst_loss", "tst_acc", "time"],
                              return_args=[]
                              )
              )
